<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Biblioteca Rhes</h1>
      </div>

      <div class="column is-12">
        <table class="table">
          <thead>
            <tr>
              <th>Título</th>
              <th>Autor</th>
              <th>Quantidade</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="book in books" v-bind:key="book.id">
              <td>
                <router-link v-bind:to="`/dashboard/books/book/${book.id}`">{{
                  book.title
                }}</router-link>
              </td>
              <td>{{ book.author.last_name }}, {{ book.author.first_name }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Books",
  data() {
    return {
      books: [],
      instances: [],
    };
  },
  mounted() {
    this.getBooks();
    this.getInstances();
  },
  methods: {
    async getBooks() {
      axios
        .get("/api/v1/books/")
        .then((response) => {
          this.books = response.data;
          console.log(this.books);
        })
        .catch((error) => {
          console.log(error.response.data.message);
        });
    },
    async getInstances() {
      axios
        .get("/api/v1/book-instances/")
        .then((response) => {
          this.instances = response.data;
          console.log(this.instances);
        })
        .catch((error) => {
          console.log(error.response.data.message);
        });
    },
  },
};
</script>