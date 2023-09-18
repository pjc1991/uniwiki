# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets, permissions

from wiki.models import Universe, WikiDocument
from .serializers import UniverseSerializer, WikiDocumentSerializer


# Standard Views


class UniWikiListView(ListView):
    template_name = 'wiki/universe_list.html'
    model = Universe
    paginate_by = 10
    permissions = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Universe.objects.filter(allowed_users=user)


class UniWikiCreateView(CreateView):
    template_name = 'wiki/universe_create.html'
    model = Universe
    fields = ['name', 'description']
    permissions = [permissions.IsAuthenticated]
    success_url = '/wiki/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not form.is_valid():
            return self.form_invalid(form)
        universe = form.save(commit=False)
        universe.owner = self.request.user
        universe.save()
        universe.allowed_users.set([self.request.user])
        return self.form_valid(form)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UniWikiDetailView(DetailView):
    template_name = 'wiki/universe_detail.html'
    model = Universe
    permissions = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Universe.objects.filter(allowed_users=user)


# --- API Views ---

class UniverseViewSet(viewsets.ModelViewSet):
    queryset = Universe.objects.all()
    serializer_class = UniverseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Universe.objects.filter(allowed_users=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, allowed_users=[self.request.user])


class WikiDocumentViewSet(viewsets.ModelViewSet):
    queryset = WikiDocument.objects.all()
    serializer_class = WikiDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return WikiDocument.objects.filter(universe__allowed_users=user)

    def perform_create(self, serializer):
        # get the current user
        user = self.request.user

        # check if the user is allowed to create a document in the universe
        if not Universe.objects.filter(allowed_users=user, id=self.request.data['universe']).exists():
            raise Exception("You are not allowed to create a document in this universe")

        # check if there is already a document with the same name in the universe
        wiki_doc = WikiDocument.objects.filter(universe__allowed_users=user, name=self.request.data['name'])

        # if more than one document with the same name exists, raise an exception
        if wiki_doc.count() > 1:
            raise Exception("There is already a document with this name in this universe")

        # if there is exactly one document with the same name, update it
        if wiki_doc.count() == 1:
            wiki_doc.update(content=self.request.data['content'])

        # if there is no document with the same name, create a new one
        if wiki_doc.count() == 0:
            serializer.save(owner=self.request.user)