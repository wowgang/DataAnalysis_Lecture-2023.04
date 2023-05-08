// AJAX(Asynchronous Javascript and XML)
// Web page의 일부분만 병경하는 방법
function changeQuote() {
    $.ajax({
      type: 'GET',
      url: '/change_quote',
      data: ' ',    // 서버로 전달할 데이터
      success: function(msg) { // msg: 서버로부터 받은 데이터
        $('#quoteMsg').html(msg);
      }
    });
  }
  function changedAddr() {
    $('#addrInput').attr('class', 'mt-2')   // input box 보이게
  }
  function addrSubmit() {
    $('#addrInput').attr('class', 'mt-2 d-none') // input box 안보이게
    let addr = $('#addrInputTag').val() //input value읽어줌
    $.ajax({
      type: 'GET', 
      url: '/change_addr',
      data: {addr: addr},     // 서버는 addr값으로 읽어라... addr은 get으로 읽어옴
      success: function(msg) {
        $('#addr').html(msg);
      }
    });
  }
  function changedWeather() {
    let addr = $('#addr').text()
    $.ajax({
      type: 'GET',
      url: '/weather',
      data: {addr: addr},
      success: function(result) {
        $('#weather').html(result);
      }

    });
  }
  function changePfofile(){
    $('#imageInput').attr('class', 'mt-2');
  }
  function imageSubmit(){
    let imageInputVal = $('#image')[0];
    let formData = new FormData();
    formData.append('image', imageInputVal.files[0]);
    $.ajax({
      type: 'POST',
      url: '/change_profile', 
      data: formData,
      processData: false,
      contentType: false,
      success: function(result) {
        $('#imageInput').attr('class', 'mt-2 d-none'); //안보이게
        let fname = 'http://127.0.0.1:5000/static/data/profile.png?q=' + result;
        $('#profile').attr('src',fname );
      }
    });
  }