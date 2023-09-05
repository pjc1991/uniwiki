Vue.component('template-form', {
    props: ['field'], template: `
<div>
    <div>
        <label v-bind:id="field.id" class="block font-medium text-gray-700" v-bind:text="field.name">
            
        </label>
    </div>
    <div class="">
        <input type="text" v-bind:id="field.id" v-bind:name="field.name" v-bind:placeholder="field.placeholder"
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

const login = new Vue({
    el: '#login',
    data: {
            fields: [{id: 'username', name: 'username', placeholder: 'Email'}, {
                id: 'password',
                name: 'password',
                placeholder: 'Password'
            }],
            loginButton: {
                name: 'Login'
            }
    },
});

