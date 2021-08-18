<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ pageTitle }}</h1>
      </div>
      <div
        :class="`column ${minCardSize}`"
        v-for="instance in instances"
        v-bind:key="instance.id"
      >
        <div class="card">
          <div class="card-image">
            <figure class="image is-4by3">
              <img
                src="https://bulma.io/images/placeholders/1280x960.png"
                alt="Placeholder image"
              />
            </figure>
          </div>
          <div class="card-content">
            <div class="content is-flex is-flex-direction-column">
              <p><strong>Título:</strong> {{ instance.book.title }}</p>

              <p><strong>Editora:</strong> {{ instance.imprint }}</p>

              <p>
                <strong>Autor:</strong> {{ instance.book.author.first_name }}
                {{ instance.book.author.last_name }}
              </p>

              <p>
                <strong>Situação:</strong>
                <span class="tag is-warning">Manutenção</span>
              </p>

              <router-link class="button is-primary" :to="`/dashboard/books/book/book-detail/${instance.id}`"
                >Ver detalhes</router-link
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <router-link class="button is-danger mt-5" :to="'/dashboard/books/'"
      >Voltar</router-link
    >
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BookInstances",
  data() {
    return {
      instances: [],
      pageTitle: "",
      minCardSize: "",
    };
  },
  mounted() {
    this.getInstances();
    // this.getAuthor();
  },
  methods: {
    async getInstances() {
      axios
        .get("/api/v1/book-instances/")
        .then((response) => {
          let data = response.data;
          this.instances = data.filter((instance) => {
            if (instance.book.id.toString() === this.$route.params.id) {
              return instance;
            }
          });

          this.pageTitle = this.instances[0].book.title;

          if (this.instances.length < 4) {
            this.minCardSize = "is-3";
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // async getAuthor() {
    //   axios
    //     .get(`/api/v1/author`)
    //     .then(response => console.log(response.data))
    //     .catch(error => console.log(error))
    // }
  },
};
</script>