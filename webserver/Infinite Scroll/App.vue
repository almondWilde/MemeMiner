var app = new Vue({
          el: '#app',
          data: {
            posts: [],
            limit: 10,
            busy: false
          },
          created(){
              this.loadMore();
          },
          methods: {
            loadMore(){
              console.log("Adding 10 more data results");
                this.busy = true;
                //change this url to connect to scraper server to return memes (and metadata)
                axios.get('https://jsonplaceholder.typicode.com/posts').then(response => {
                  const append = response.data.slice(
                    this.posts.length,
                    this.posts.length+ this.limit
                  );
                  this.posts = this.posts.concat(append);
                  this.busy = false;
                });
            }
          }
        });
