services.component('services-cart', {
    delimiters: ['[[', ']]'],
    template: 
      /*html*/`
        <div v-for="data in cartdata" :key="data.id" class="col-lg-4 col-md-6 col-sm-6">
            <div @click="ShowService(data)" class="service-block mb-5">
                <img :src="data.img" alt="" class="img-fluid"> 
                <div class="content">
                    <h4 class="mt-4 mb-2 title-color">[[data.title]]</h4>
                    <p class="mb-4" v-html="data.description.substring(0,80)"></p>
                </div>
            </div>
        </div>
        <services-details v-if="popupdata.visible" :popupdata="popupdata" :hide="hideService"/>
        `,
    data() {
      return {
        cartdata: '',
        popupdata:{
            data: '',
            visible: false
        }
      }
    },
    methods:{
        ShowService(data){
            this.popupdata.data = data
            this.popupdata.visible = true
        },
        hideService(){
            this.popupdata.visible = false
        }
    },
    beforeMount() {
        axios.get(`http://127.0.0.1:8000/api/services/`)
            .then((res) => {
                this.cartdata = res.data
            })
            .catch((error) => {
                console.log(error)
            })
    },
      
})