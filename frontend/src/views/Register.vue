<template>
  <div class="auth-wrapper auth-v2">
    <div class="auth-inner">
      <!-- brand logo -->
      <router-link to="/" class="brand-logo d-flex align-center">
        <v-img :src="appLogo" max-height="30px" max-width="30px" alt="logo" contain class="me-3"></v-img>

        <h2 class="text--primary">
          {{ appName }}
        </h2>
      </router-link>
      <!--/ brand logo -->

      <v-row class="auth-row ma-0">
        <v-col lg="8" class="d-none d-lg-block position-relative overflow-hidden pa-0">
          <div class="auth-illustrator-wrapper">
            <!-- triangle bg -->
            <img
              height="362"
              class="auth-mask-bg"
              :src="require(`@/assets/images/misc/mask-v2-${$vuetify.theme.dark ? 'dark' : 'light'}.png`)"
            />

            <!-- tree -->
            <v-img height="226" width="300" class="auth-tree" src="@/assets/images/misc/tree-2.png"></v-img>

            <!-- 3d character -->
            <div class="d-flex align-center h-full pa-16 pe-0">
              <v-img
                contain
                max-width="100%"
                height="600"
                class="auth-3d-group"
                :src="require(`@/assets/images/3d-characters/illustration-john.png`)"
              ></v-img>
            </div>
          </div>
        </v-col>

        <v-col lg="4" class="d-flex align-center auth-bg pa-10 pb-0">
          <v-row>
            <v-col cols="12" sm="8" md="6" lg="12" class="mx-auto">
              <v-card flat>
                <v-card-text>
                  <p class="text-2xl font-weight-semibold text--primary my-2">Sign Up</p>
                  <p class="mb-2">Create your account here</p>
                </v-card-text>

                <!-- login form -->
                <v-card-text>
                  <v-form ref="registerForm" @submit.prevent="handleFormSubmit">
                    <v-text-field
                      v-model="email"
                      dense
                      outlined
                      :error-messages="errorMessages.email"
                      :rules="[validators.required, validators.emailValidator]"
                      label="Email"
                      placeholder="Email"
                      hide-details="auto"
                      class="mb-6"
                    ></v-text-field>

                    <v-text-field
                      v-model="first_name"
                      dense
                      outlined
                      :error-messages="errorMessages.first_name"
                      :rules="[validators.required]"
                      label="First Name"
                      placeholder="first name"
                      hide-details="auto"
                      class="mb-6"
                    ></v-text-field>
                    <v-text-field
                      v-model="last_name"
                      dense
                      outlined
                      :error-messages="errorMessages.last_name"
                      :rules="[validators.required]"
                      label="Last Name"
                      placeholder="last name"
                      hide-details="auto"
                      class="mb-6"
                    ></v-text-field>

                    <v-radio-group hide-details="auto" :rules="[validators.required]" row>
                      <v-radio label="Male" value="radio-1"></v-radio>
                      <v-radio label="Female" value="radio-2"></v-radio>
                    </v-radio-group>
                    Race category:
                    <v-btn-toggle class="mt-2" mandatory borderless color="primary" v-model="race_category">
                      <v-btn> A </v-btn>

                      <v-btn>B </v-btn>

                      <v-btn> C</v-btn>

                      <v-btn> D</v-btn>
                    </v-btn-toggle>
                    <!-- <v-text-field
                      v-model="password"
                      dense
                      outlined
                      :type="isPasswordVisible ? 'text' : 'password'"
                      label="Password"
                      :error-messages="errorMessages.password"
                      placeholder="Password"
                      :rules="[validators.required, validators.passwordValidator]"
                      :append-icon="isPasswordVisible ? icons.mdiEyeOffOutline : icons.mdiEyeOutline"
                      hide-details="auto"
                      class="mb-2 mt-2"
                      @click:append="isPasswordVisible = !isPasswordVisible"
                    ></v-text-field> -->

                    <v-checkbox hide-details class="mt-0">
                      <template #label>
                        <div class="d-flex align-center flex-wrap">
                          <span class="me-2">I agree to</span
                          ><a href="javascript:void(0)">privacy policy &amp; terms</a>
                        </div>
                      </template>
                    </v-checkbox>

                    <v-btn block color="primary" type="submit" class="mt-6"> Sign Up </v-btn>
                  </v-form>
                </v-card-text>

                <!-- create new account  -->
                <v-card-text class="d-flex align-center justify-center flex-wrap mt-2">
                  <p class="mb-0 me-2">Already have an account?</p>
                  <router-link :to="{ name: 'auth-login' }"> Sign in instead </router-link>
                </v-card-text>

                <!-- divider -->
                <v-card-text class="d-flex align-center mt-2">
                  <v-divider></v-divider>
                  <span class="mx-5">or</span>
                  <v-divider></v-divider>
                </v-card-text>

                <!-- social links -->
                <v-card-actions class="d-flex justify-center">
                  <v-btn v-for="link in socialLink" :key="link.icon" icon disabled class="ms-1">
                    <v-icon :color="$vuetify.theme.dark ? link.colorInDark : link.color">
                      {{ link.icon }}
                    </v-icon>
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
// eslint-disable-next-line object-curly-newline
import { mdiFacebook, mdiTwitter, mdiGithub, mdiGoogle, mdiEyeOutline, mdiEyeOffOutline } from '@mdi/js'
// eslint-disable-next-line object-curly-newline
import { required, emailValidator, passwordValidator, alphaValidator } from '@core/utils/validation'
import { ref, getCurrentInstance } from '@vue/composition-api'
import axios from '@axios'
import store from '@/store'
import router from '@/router'

import { useRouter } from '@core/utils'
import themeConfig from '@themeConfig'

export default {
  setup() {
    // Template Refs
    const registerForm = ref(null)

    const vm = getCurrentInstance().proxy
    const { router } = useRouter()

    const isPasswordVisible = ref(false)
    const email = ref('')
    const username = ref('')
    const first_name = ref('')
    const last_name = ref('')
    const password = ref('')
    const race_category = ref('')
    const errorMessages = ref([])
    const socialLink = [
      {
        icon: mdiFacebook,
        color: '#4267b2',
        colorInDark: '#4267b2',
      },
      {
        icon: mdiTwitter,
        color: '#1da1f2',
        colorInDark: '#1da1f2',
      },
      {
        icon: mdiGithub,
        color: '#272727',
        colorInDark: '#fff',
      },
      {
        icon: mdiGoogle,
        color: '#db4437',
        colorInDark: '#db4437',
      },
    ]

    const handleFormSubmit = () => {
      const isFormValid = registerForm.value.validate()

      if (!isFormValid) return

      store
        .dispatch('signup', { username: "asdasdd", email: email.value, password: password.value })
        .then(data => {
          router.push({'name': 'auth-login'})

        })
        .catch(error => {
          // TODO: Next Update - Show notification
          console.error('Oops, Unable to Register!')
          console.log('error :>> ', error.response)
          errorMessages.value = error.response.data.error
        })
    }

    return {
      isPasswordVisible,
      username,
      email,
      first_name,
      last_name,
      password,
      race_category,
      errorMessages,
      handleFormSubmit,
      socialLink,
      icons: {
        mdiEyeOutline,
        mdiEyeOffOutline,
      },
      validators: {
        required,
        emailValidator,
        passwordValidator,
        alphaValidator,
      },

      // themeConfig
      appName: themeConfig.app.name,
      appLogo: themeConfig.app.logo,

      // Template Refs
      registerForm,
    }
  },
}
</script>

<style lang="scss" scoped>
@import '@core/preset/preset/pages/auth.scss';
</style>
