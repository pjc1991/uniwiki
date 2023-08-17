# Create your views here.
from django.views.generic import ListView, DetailView
from rest_framework import viewsets, permissions

from wiki.models import Universe, WikiDocument
from .serializers import UniverseSerializer, WikiDocumentSerializer


# Standard Views


class UniWikiListView(ListView):
    template_name = 'wiki/universe_list.html'
    model = Universe
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
        universe = Universe.objects.get(id=self.request.data['universe'])
        if not universe.allowed_users.filter(id=self.request.user.id).exists():
            raise Exception("You are not allowed to create a document in this universe")
        serializer.save(owner=self.request.user, universe=universe)
