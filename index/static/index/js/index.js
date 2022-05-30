let index = Vue.createApp({
  delimiters: ['[[', ']]'],
    data() {
      return {
        // csrf: document.getElementsByName('csrfmiddlewaretoken').value,
        messageform:{
          name: "",
          email: "",
          phone: "",
          message: ""
        },
        messagebox:{
          visible: false,
          message: Object
        }
      }
    },
    methods:{
      Go_to_appoinment(place){
        let element = this.$refs[place];
        let GO = element.offsetTop;
        window.scrollTo(0, GO);
      },
      sendmsg(){
        axios.post('http://127.0.0.1:8000/api/index/', this.messageform)
        .then((res) => {
          console.log(this.messageform)
        })
        .catch(function (error) {
        console.log(error);
        console.log(this.messageform)
        });
  
      },
      msgboxShow(){
        this.messagebox.visible =! this.messagebox.visible
        this.messagebox.message = this.errormsg()
      },
      // TO RESET THE FORM
      resetform(form){
        for (const key in form){
          this.messageform[key] = ''
        }
      },
      // TO SHOW WHICH INPUT IS EMPTY 
      errormsg(){
        for (const key in this.messageform){
          if (this.messageform[key] == ''){
            return {
              first: `${key.toUpperCase()} Error`, 
              second: `Did you forgot to put your ${key}`
            }
          }
        }
        this.sendmsg()
        // this.resetform(this.messageform)
        return {
          first: `Message Submited`,
          second: `Thank you for getting in touch! We will review your message and reply you back soon.`
        }
      }
      // END
    },
})


index.component('Notification-box', {
  delimiters: ['[[', ']]'],
    data() {
      return {
        
      }
    },
    template: 
    /*html*/`
    <!--  -->
    <div v-if="messagebox.visible" class="overlays">
				<div class="popups">
					<h2>[[messagebox.message.first]]</h2>
					<a class="close" @click="msgboxShow()">&times;</a>
					<div class="content" style="font-size: 120%">
						[[messagebox.message.second]]
					</div>
				</div>
		</div>
		<!--  -->`
})
