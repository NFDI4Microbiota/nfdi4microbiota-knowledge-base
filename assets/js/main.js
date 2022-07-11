  

  $(document).ready(function(){
//    var search_pages = SimpleJekyllSearch({
//    searchInput: document.getElementById('search-input'),
//    resultsContainer: document.getElementById('results-container'),
//    searchResultTemplate: "<a href='{url}' class='list-group-item list-group-item-action'>{title}</a>",
//    json: '/search.json'
//  })
    //events registration
    $('form').delegate('.OthersTextBox', 'change', function(){ OtherSelect(this);});
    $('form').delegate('.otherTxtBox', 'focusout', function(){ ChangeSelect(this); });
    
    // $('.OthersTextBox').on('change', function(){  });

    $(window).scroll(function() {
      if ($(window).scrollTop() > 50) {
        $('.navbar').addClass('fixed-top');
      }
      if ($(window).scrollTop() < 51) {
        $('.navbar').removeClass('fixed-top');
      }
    });
    // to enable DataTable on the table containing .DataTable class only
    $('.DataTable').DataTable();
    $('.DataTableSorted').DataTable({      
      ordering: false
    });

    $("#use-case-form").validate(
        {
        errorClass: "is-invalid"});
      $.validator.messages.required = '<small style="color:red;"> This Field is required </small>';

      AutoActivateFirstChildTab();
  // use case form validation
  //$("#use-case-form").submit(function( event ){
  //  if (!form.checkValidity()) {
  //    event.preventDefault()
  //    event.stopPropagation()
  //  }
  //
  //  form.classList.add('was-validated')
  // for search functionality in Select list
//   $('.SearchSelect').select2({
//     placeholder: 'Select an option',
//     allowClear: true
//   });  
  });

// tab UI first child auto active

function AutoActivateFirstChildTab()
{
  $('.nav-pills').children().eq(0).addClass('active');
  $('.tab-content').children().eq(0).addClass('active');  
}

  // General Others TextBox Generation from Selection
  function OtherSelect(Select){
    if($(Select).val() == 'Others'){
        $.when(AppendElements(Select)).then();

    }
    else{
        RemoveExtras(Select);
    }
  }

  function RemoveExtras(Select)
  {
    $(Select).closest('.row').children().eq(1).remove();
  }

  function AppendElements(Select)
  {
    $(Select).parent().removeClass('row');
    $(Select).parent().addClass('row');
    var SelectParentHTML = $(Select).parent().html();
    SelectParentHTML = '<div class="col-md">' + SelectParentHTML + "</div>";
    $(Select).closest('.OtherTbParent').html(SelectParentHTML+CreateInputWithLabel('Other-'+$(Select).attr('id')));
    $('#Other-'+$(Select).attr('id')).focus();
  }

  function CreateInputWithLabel(Identifier){
return   `<div class="col-md">
<label for="last-name" class="form-label">Specify Others</label>
<input type="${Identifier}" data-impact="${Identifier}" class="form-control otherTxtBox" id="Other-${Identifier}" aria-describedby="Other-${Identifier}" required="">
</div>`;
  }

  function ChangeSelect(TxtBox)
  {
      if($(TxtBox).val() != ''){
        $(TxtBox).parent().parent().children().eq(0).find('select').append(`<option value="${$(TxtBox).val()}">${$(TxtBox).val()}</option>`);
        $(TxtBox).parent().parent().children().eq(0).find('select').val($(TxtBox).val());
      }
     
  }

  
