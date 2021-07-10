<template>
  <v-app id="inspire">
    <v-main>
      <v-container class="fill-height">
        <v-row align="center" justify="center">
          <v-col cols="12" sm="5">
            <v-card :disabled="cardLoader" :loading="cardLoader" class="rounded-lg" outlined  elevation="0">
              <v-card-text>
                <!-- <b>Validation orm {{validationForm}}</b> -->
                <v-form ref="validationFormRef" v-model="validationForm">
                <v-row class="pt-10">
                  <v-col cols="12" sm="12"> Image </v-col>
                </v-row>
                <v-row cols="12" sm="12">
                  <v-col>
                    <h1
                      style="color: black; font-family: 'Open Sans', sans-serif"
                    >
                      Create your {{ Company }} Account
                    </h1>
                  </v-col>
                </v-row>
                <v-row > 
                  <v-col cols="12" sm="6"  >
                    <v-text-field hide-details  :rules="validation.FirstNameValidation" dense outlined label="First Name"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" >
                    <v-text-field hide-details :rules="validation.FirstNameValidation" dense outlined label="Last Name"></v-text-field>
                  </v-col>
                </v-row>
                <v-row > 
                  <v-col cols="12" sm="12" >
                    <v-text-field hide-details :rules="validation.UserNameValidation" dense outlined label="Username"></v-text-field>
                  </v-col>
                
                </v-row>
                <v-row > 
                  <v-col cols="12" sm="6"  >
                    <v-text-field hide-details :rules="validation.PasswordValidation" :type="showPassword ? 'text' : 'password' " dense outlined label="Password"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" >
                    <v-text-field hide-details :rules="validation.ConfirmPasswordValidation" :type="showPassword ? 'text' : 'password'" dense outlined label="Confirm"></v-text-field>
                  </v-col>
                  <v-checkbox class="pl-3" v-model="showPassword" label="Show Password"></v-checkbox>
                </v-row>
                </v-form>
              </v-card-text>
              <v-card-actions> 
                <v-btn
                  text
                  to="/Signin"
                  color="#1a73e8"
                  class="text-none pa-4 font-weight-meduim pl-4"
                  style="letter-spacing: 0.0107142857em"
                  >Sign in insted</v-btn
                >
                <v-spacer></v-spacer>
                <v-btn
                  color="#1a73e8"
                  class="text-none pa-4 white--text font-weight-meduim"
                  style="letter-spacing: 0.0107142857em"
                  @click="CreateAccountValidation"
                  >Next</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-col>
          <!-- <v-col cols="12" sm="5">
            <p style="color: black; font-family: 'Open Sans', sans-serif">One account. All of  {{ Company }} working for you.</p>
          </v-col> -->
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
      showPassword: false,
      cardLoader: false,
      validationForm: "",

      validation: {
        FirstNameValidation: [(v) => !!v || "First Name is required"],
        LastNameValidation: [(v) => !!v || "Last Name is required"],
        UserNameValidation: [(v) => !!v || "User Name is required"],
        PasswordValidation: [(v) => !!v || "Password is required"],
        ConfirmPasswordValidation: [(v) => !!v || "Confirm Password is required"],
      },
    };
  },
  methods: {
    CreateAccountValidation() {
      if(this.$refs.validationFormRef.validate()){
              this.cardLoader = true;
      }
    },
  },
};
</script>

