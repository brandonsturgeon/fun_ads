function highlight()
{
    var phrase = "{TEXT}";
    inputText = document.getElementById("content-text");
    console.log(inputText);
    var innerHTML = inputText.innerHTML;

    var split_up = [];
    for (i = 0; i < phrase.length; i++) {
      letter = phrase.charAt(i);
      found = innerHTML.indexOf(letter);
      slice = innerHTML.slice(0,found);
      split_up.push(slice);
      split_up.push("<span class='highlight'>"+letter+"</span>");
      innerHTML = innerHTML.slice(found+1, innerHTML.length);
    }
    inputText.innerHTML = split_up.join("");
    console.log(split_up);
}

highlight();


//      var letter = phrase.charAt(i);
//      var slice = innerHTML.slice(last_index, innerHTML.length);
//      var found = slice.indexOf(letter);
//      console.log(letter);
//      console.log(slice);
//      console.log("");
