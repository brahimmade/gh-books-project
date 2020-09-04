var app = new Vue({
    el: '#bookReader',
    delimiters: ['[[',']]'],//default delimiters are same as django template so need to change
    data: {
        books: [],
        loading: false,
    },
    mounted: function() {
        this.getBooks();           
    },
    methods: {
        getBooks: function() {
        
        this.loading = true;
        axios
            .get('/bookapi/books/')
            .then(response => {
                this.books = response.data
            })
            .catch(error => {
                console.log(error)
                this.errored = true
            })
            .finally(() => this.loading = false)

        }
    },
    filters: {
        subStr: function(wholeString) {//return file name instead of full path
            return wholeString.substring((wholeString.lastIndexOf("/")+1),wholeString.length);
            }
    }
})