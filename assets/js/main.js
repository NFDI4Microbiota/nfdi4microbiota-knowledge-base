$(document).ready(function () {

  //AutoActivateFirstChildTab();
  GenerateScrollSpy();
  ChangeMenuTablets();
});


function ChangeMenuTablets(){
  var headingtext = $('#content').text()
  $('.active').removeClass('active');
  var selectedelement = $('.bd-links-link').filter(function(){  return $(this).text() === headingtext; });
  $(selectedelement).addClass('active');
  // $('.bd-links-link:contains("'+ headingtext +'")').addClass('active');
}

// tab UI first child auto active

function AutoActivateFirstChildTab() {
  $('.fw-normal').children().children().eq(0).addClass('active');
  // $('.tab-content').children().eq(0).addClass('active');  
}

// General Others TextBox Generation from Selection
function OtherSelect(Select) {
  if ($(Select).val() == 'Others') {
    $.when(AppendElements(Select)).then();

  }
  else {
    RemoveExtras(Select);
  }
}

function RemoveExtras(Select) {
  $(Select).closest('.row').children().eq(1).remove();
}

function AppendElements(Select) {
  $(Select).parent().removeClass('row');
  $(Select).parent().addClass('row');
  var SelectParentHTML = $(Select).parent().html();
  SelectParentHTML = '<div class="col-md">' + SelectParentHTML + "</div>";
  $(Select).closest('.OtherTbParent').html(SelectParentHTML + CreateInputWithLabel('Other-' + $(Select).attr('id')));
  $('#Other-' + $(Select).attr('id')).focus();
}

function CreateInputWithLabel(Identifier) {
  return `<div class="col-md">
<label for="last-name" class="form-label">Specify Others</label>
<input type="${Identifier}" data-impact="${Identifier}" class="form-control otherTxtBox" id="Other-${Identifier}" aria-describedby="Other-${Identifier}" required="">
</div>`;
}

function ChangeSelect(TxtBox) {
  if ($(TxtBox).val() != '') {
    $(TxtBox).parent().parent().children().eq(0).find('select').append(`<option value="${$(TxtBox).val()}">${$(TxtBox).val()}</option>`);
    $(TxtBox).parent().parent().children().eq(0).find('select').val($(TxtBox).val());
  }

}
function GenerateScrollSpy() {
  let currentUl = $('<ul></ul>'); // Start with an empty list
  let currentH = null; // Track the current <h1>

  $('h2, h3').each(function (index, element) {
    const tag = $(element).prop('tagName');
    
    if (tag === 'H2') {
      currentH = $('<li><a href="#' + $(element).attr('id') + '">' + $(element).text() + '</a></li>');
      currentUl = $('<ul></ul>'); // Create a new <ul> for nested h2 elements
      currentH.append(currentUl);
      $('#TableOfContents').children().eq(0).append(currentH);
    } else if (tag === 'H3' && currentH) {
      currentUl.append('<li><a style="font-size:0.8rem" href="#' + $(element).attr('id') + '">' + $(element).text() + '</a></li>');
    }
  }); 
}

