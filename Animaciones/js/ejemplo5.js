const addTodo = () => {
    const ul = document.getElementsByTagName('ul')[0];
    const input1 = document.getElementById('todoInput').value;
    const input2 = document.getElementById('todo').value;
    const input3 = document.getElementById('todo2').value;
  
    if (input1.length > 0) {
      const li = document.createElement('li');
  
      const animations = [
        'animate__animated',
        'animate__fadeIn'
      ];
  
      li.classList.add(...animations);
   li.appendChild(document.createTextNode(input1 +' '));
   li.appendChild(document.createTextNode(input2+' '));
     li.appendChild(document.createTextNode(input3));
  
      ul.appendChild(li);
  
      document.getElementById('todoInput'+' '+'todo'+ 'todo2').value = '';
    }
  };