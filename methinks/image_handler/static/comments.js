axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
var my_form = document.getElementById("my_form");
var image_id = JSON.parse(document.getElementById('image_id').textContent);
var app = Vue.createApp({
data() {
    const my_data = {
        comments: [],
        name: '',
        email: '',
        body: '',
    }
    return my_data
},
methods: {
    getComments() {
        var self = this;
        axios.get(`/api/comments/search/${image_id}`)
            .then(function(response) {
                self.comments = response.data
                console.log(self.comments)
            })
            .catch(function(error){
                console.log(error);
            })
    },
    registerComment() {
        const data = {
            image: image_id,
            name: this.name,
            email: this.email,
            body: this.body, 
        };
        console.log(data);
        var self = this;
        axios.post('/api/comments/register', data)
            .then(function(response) {
                console.log(response)
            })
            .then(function(response){
                self.getComments()
            })
            .catch(function(error){
                console.log(error);
            })
    },
},
mounted() {
    this.getComments(image_id);
},
compilerOptions: {
    delimiters: ["[[", "]]"]
}
}).mount('#app');