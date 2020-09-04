var app = new Vue({
    el: '#uploading',
    delimiters: ['[[',']]'],
    data: {
        books: [],
        loading: false,
        currentBook: {},
        message: null,
        newBook: { 'book_title': null, 'file': null },
        upload: null,
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
                this.loading = false;
            })
            .catch(error => {
                console.log(error)
                this.loading = false;
            })
            .finally(() => this.loading = false)
        },
        getBook: function(id) {
        this.loading = true;
        axios
            .get('/bookapi/books/'+id+'/')
            .then(response => {
                this.currentBook = response.data;
                $("#editBookModal").modal('show');
                this.loading = false;
            })
            .catch(error => {
                console.log(error)
                this.loading = false;
            })
            .finally(() => this.loading = false)
        },
        addBook: function() {
        this.loading = true;
        let config = {
            header : {
             'Content-Type' : 'multipart/form-data'
           }
          }
        var upload = new FormData();
        upload.append('book_title', this.newBook.book_title);
        upload.append('file', this.$refs.addfile.files[0]);
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
        axios
            .post('/bookapi/books/', upload, config)
            .then(response => {
                this.loading = false;
                this.getBooks();
                $('#addBookModal').modal('hide');
            })
            .catch(error => {
                console.log(error)
                this.loading = false;
            })
            .finally(() => this.loading = false)
        },
        updateBook: function() {
        this.loading = true;
        let config = {
            header : {
             'Content-Type' : 'multipart/form-data'
           }
          }
        var upload = new FormData();
        upload.append('book_title', this.currentBook.book_title);
        upload.append('file', this.$refs.updatefile.files[0]);
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
        axios
            .put('/bookapi/books/'+this.currentBook.id+'/', upload, config)
            .then(response => {
                this.loading = false;
                this.currentBook = response.data;
                this.getBooks();
                $('#editBookModal').modal('hide');
            })
            .catch(error => {
                console.log(error)
                this.loading = false;
            })
            .finally(() => this.loading = false)
        },
        deleteBook: function(id) {
        this.loading = true;
        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
        axios
            .delete('/bookapi/books/'+id+'/')
            .then(response => {
                this.loading = false;
                this.getBooks();
            })
            .catch(error => {
                console.log(error)
                this.loading = false;
            })
            .finally(() => this.loading = false)
        }
    }
})