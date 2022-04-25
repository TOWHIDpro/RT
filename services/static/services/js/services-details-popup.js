services.component('services-details', {
    delimiters: ['[[', ']]'],
    template: 
      /*html*/`
      <div class="popup-main">
        <input class="modal-state" id="modal-1" type="checkbox" checked>
        <div class="modal-details">
            <div class="modal__inner">
                <label @click="hide" class="modal__close"></label>
                <h2>[[popupdata.data.title]]</h2>
                <img class="cart-image" :src="popupdata.data.img" alt="" /> <hr>
                <div v-html="popupdata.data.description"></div>
            </div>
        </div>
      </div>`,
  
    props: {
      popupdata: Object,
      hide: Function,
    },
    
      
})