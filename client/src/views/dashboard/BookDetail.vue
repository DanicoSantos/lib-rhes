<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ pageTitle }}</h1>
      </div>
      <div class="column is-4">
        <figure class="image">
          <img
            src="https://via.placeholder.com/200x300"
            alt=""
            style="width: 200px; height: 300px"
          />
        </figure>
      </div>
      <div class="column is-8">
        <div
          class="container is-flex is-flex-direction column"
          v-for="item in bookInstance"
          v-bind:key="item.id"
        >
            <p><strong>Autor:</strong> {{ item.book.author.first_name }} {{ item.book.author.last_name }}</p>
            <p><strong>Status: </strong> <span class="tag is-warning">{{ item.status }}</span></p>
            <p><strong>Gêneros:</strong> {{ item.book.display_genre }}</p>
        </div>
      </div>
    </div>
    <router-link
      class="button is-danger mt-5"
      :to="`/dashboard/books/book/${this.bookId}`"
      >Voltar</router-link
    >
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BookDetail",
  data() {
    return {
      bookInstance: [],
      pageTitle: "",
      bookId: "0",
    };
  },
  mounted() {
    this.getInstance();
  },
  methods: {
    async getInstance() {
      axios
        .get(`/api/v1/book-instances/${this.$route.params.id}`)
        .then((response) => {
          this.bookInstance = response.data;

          this.pageTitle = this.bookInstance.book.title;

          this.bookId = this.bookInstance.book.id;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>