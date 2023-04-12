function getChecked() {
  let result = "";
  let checkboxes = document.querySelectorAll(".form-check-input");
  for (let i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      result += checkboxes[i].id.toLowerCase() + "+";
    }
  }

  let link = document.querySelector("#filter_link");

  link.href = link.href + result;


}