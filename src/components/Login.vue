<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height pa-10">
        <v-row align="center" justify="center">
          <v-col cols="12" sm="5">
            <form ref="forms" method="post">
              <input name="username" :value="username" type="hidden" />
              <input name="password" :value="password" type="hidden" />
              <v-card loading="loagin_loader" class="rounded-lg" outlined>
                <v-card-text>
                  <v-row class="pt-10">
                    <v-col cols="12" sm="12">
                      <center>Image</center>
                    </v-col>
                  </v-row>
                  <v-row cols="12" sm="12">
                    <v-col>
                      <center>
                        <h1
                          style="
                            color: black;
                            font-family: 'Open Sans', sans-serif;
                          "
                        >
                          Sign in
                        </h1>
                      </center>
                    </v-col>
                  </v-row>
                  <v-row cols="12" sm="12">
                    <v-col>
                      <center>
                        <h3 style="font-family: 'Open Sans', sans-serif">
                          Use your {{ Company }} account
                        </h3>
                      </center>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-alert v-if="loginStatus != -1" dense color="red">
                        {{ getErrorMessage(loginStatus) }}
                      </v-alert>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-form>
                        <v-row>
                          <v-col>
                            <v-text-field
                              outlined
                              dense
                              v-on:keyup.enter="$refs.forms.submit"
                              :hide-details="hideUserNameField"
                              :rules="UsernameRule"
                              v-model="username"
                              label="Username"
                              type="text"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                        <v-row>
                          <v-col>
                            <v-text-field
                              outlined
                              dense
                              v-on:keyup.enter="$refs.forms.submit"
                              :hide-details="hideUserNameField"
                              label="Password"
                              v-model="password"
                              type="password"
                            ></v-text-field>
                          </v-col>
                        </v-row>
                      </v-form>
                      <v-btn
                        text
                        color="#1a73e8"
                        class="text-none pa-4 font-weight-meduim pl-2"
                        style="letter-spacing: 0.0107142857em"
                        >Forgot username?</v-btn
                      >
                    </v-col>
                  </v-row>
                </v-card-text>
                <v-card-actions>
                  <v-btn
                    text
                    to="/Signup"
                    color="#1a73e8"
                    class="text-none pa-4 font-weight-meduim pl-4"
                    style="letter-spacing: 0.0107142857em"
                    >Create account</v-btn
                  >
                  <v-spacer></v-spacer>
                  <v-btn
                    type="submit"
                    @click="loagin_loader = true"
                    color="#1a73e8"
                    class="pa-4 white--text font-weight-meduim"
                    style="letter-spacing: 0.0107142857em"
                    >Login</v-btn
                  >
                </v-card-actions>
              </v-card>
            </form>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>







<script>
import { UtilityMixin } from "../mixins/utility";

export default {
  mixins: [UtilityMixin],
  data() {
    return {
      hideUserNameField: true,
      env: process.env.VUE_APP_Backed_API,
      loginStatus: -1,
      loagin_loader: false,
      // Rules
      UsernameRule: [],
      // Values
      username: "",
      password: "",
    };
  },
  mounted() {
    // Login Check
    if (this.$route.query.login == "failed") {
      this.loginStatus = 0;
    }
  },
  methods: {
    getErrorMessage(Status) {
      if (Status == 0) {
        return "Username or Password Incorrect";
      }
    },
  },
};
</script>

<style>
</style>