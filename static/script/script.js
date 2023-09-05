Vue.component('template-form', {
    props: ['field'], template: `
<div>
    <div>
        <label :id="field.id" class="block font-medium text-gray-700" d:text="field.name">
            
        </label>
    </div>
    <div class="">
        <input type="text" :id="field.id" :name="field.name" :placeholder="field.placeholder"
               class="w-full p-2 rounded border focus:border-blue-400 focus:ring focus:ring-blue-200 focus:ring-opacity-50">
    </div>
</div>
    `
})

Vue.component('template-button', {
    props: ['button'], template: `
<div>
    <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200 focus:ring-opacity-50">{{ button.name }}</button>
</div>
`
})

Vue.component('login-form', {
    props: ['loginForm'],
    template: `
<div id="login-form" class="bg-gray-100 p-8 rounded shadow-md w-1/3">
    <template-form v-for="field in loginForm[fields]" :field="field" v-bind:key="field.id" ></template-form>
    <template-button v-bind:button="loginForm.loginButton"></template-button>
</div>
   `,
    components: {
        'template-form': 'template-form',
        'template-button': 'template-button'
    }
});

const login = new Vue({
    el: '#login',
    data: {
        loginInfo: {
            fields: [
                {id: 'username', name: 'username', placeholder: 'Email'},
                {id: 'password', name: 'password', placeholder: 'Password'}],
            loginButton: {name: 'Login'}
        }
    },
});

