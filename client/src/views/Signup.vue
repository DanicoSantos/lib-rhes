<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Signup</h1>
        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                class="input"
                v-model="username"
              />
            </div>
          </div>

          <div class="field">
            <label for="">Password</label>
            <div class="control">
              <input
                type="password"
                name="password1"
                class="input"
                v-model="password1"
              />
            </div>
          </div>

          <div class="field">
            <label for="">Repeat password</label>
            <div class="control">
              <input
                type="password"
                name="password2"
                class="input"
                v-model="password2"
              />
            </div>
          </div>

          <!-- Notification -->
          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-success">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
  name: "Signup",
  data() {
    return {
      username: "",
      password1: "",
      password2: "",
      errors: [],
    };
  },
  methods: {
    submitForm() {
      this.error = []

      if (this.username === '') {
        this.errors.push('The username is missing')
      }

      if (this.password1 === '') {
        this.errors.push('The password is too short')
      }

      if (this.password1 !== this.password2) {
        this.errors.push('The passwords do not match')
      }

      // Form handling
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password1
        }

        // Server request
        axios
          .post('/api/v1/users/', formData)
          .then(response => {
            toast({
              message: 'Account was created, please log in',
              type: 'is-success',
              dismissible: true,
              pauseOnHover: true,
              
            })
          })
      }
    },
  },
};
</script>