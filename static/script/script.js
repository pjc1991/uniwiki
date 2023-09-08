Vue.component('template-form', {
    props: ['field'], template: `
<div class="">
    <div >
        <label :id="field.id" class="block font-medium text-gray-700" d:text="field.name">
        </label>
    </div>
    <div class="">
        <input type="text" :id="field.id" :name="field.name" :placeholder="field.placeholder"
               class="w-full  p-2 rounded border focus:border-blue-400 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
    </div>
</div>
    `
})

Vue.component('template-button', {
    props: ['button'],
    template: `
<div class="grow">
    <button type="submit" v-bind:class="button.color" :id="button.id" class="w-full text-white p-2 rounded hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200 focus:ring-opacity-50">{{ button.name }}</button>
</div>
`
})



Vue.component('login-form', {
    props: ['login-form-props'],
    template: `
<div id="login-form" class="bg-gray-100 p-8 rounded shadow-md w-1/3">
    <template-form v-for="field in loginFormProps.fields" :field="field" v-bind:key="field.id" ></template-form>
    <div class="">
        <template-button :button="loginFormProps.buttons[0]" @click="alert('test')"></template-button>
        <template-button :button="loginFormProps.buttons[1]" @click="alert('test')"></template-button>
    </div>
</div>
   `,
});



const app = new Vue({
    el: '#app',
    data: {
        loginInfo: {
            fields: [
                {id: 'username', name: 'username', placeholder: 'Email'},
                {id: 'password', name: 'password', placeholder: 'Password'}],
            buttons: [
                {id: 'login', name: 'login', placeholder: 'Login', color: 'bg-blue'},
                {id: 'signup', name: 'signup', placeholder: 'Sign Up', color: 'bg-green'}]
        }
    },
});



