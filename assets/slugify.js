/* taking the names of the slug and title input fields and storing them in a const variable */
const titleinput = document.querySelector('input[name=title]');
const sluginput = document.querySelector('input[name=slug]');

const slugify = (val)=>{ //taking the value in slug field
    return val.toString().toLowerCase().trim() //converting the value to String,lowercase and removing whitesapaces
    .replace(/&/g,'-and-') //replace $ with '-and-' which is url friendly
    .replace(/[\s\W-]+/g,'-') //replace spaces,non word characters and dashes with a single dash

};
 
titleinput.addEventListener('keyup',(e)=>{ //add event listener
    sluginput.setAttribute('value',slugify(titleinput.value));
});