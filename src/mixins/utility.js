
export const UtilityMixin = {
    data(){
        return{
            Company: process.env.VUE_APP_Company_Name
        }
    },
    filters: {
        uppercase: function(v) {
          return v.toUpperCase();
        }
      },
}