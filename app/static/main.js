document.getElementById('estimation').addEventListener('click', function(e) {
    e.preventDefault();
    const task_size = document.getElementById('task-size').value;
    const task_complexity = document.getElementById('task-complexity').value;
    const task_type = document.getElementById('task-type').value;
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/get_estimate', true);
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            const response = JSON.parse(xhr.responseText);
            if (xhr.status === 200 && response.estimate !== undefined) {
                if (typeof response.estimate == 'number'){
                    document.getElementById('result').innerHTML = '<h3>Estimated Effort: ' + response.estimate + '</h3>' +
                                                                    '<p>Confidence Level: ' + response.confidence_level + '</p>';
                    document.getElementById('estimated-effort').value = response.estimate;
                    }
                else{
                    document.getElementById('result').innerHTML = '<h3>Hestorical data not found!!</h3>'
                }    
            } else {
                document.getElementById('result').innerHTML = '<h3>' + response.message + '</h3>';
            }
        }
    };
    xhr.onerror = function() {
        document.getElementById('result').innerHTML = '<h3>An error occurred while estimating.</h3>';
    };
    xhr.send(JSON.stringify({task_complexity: task_complexity, task_size: task_size, task_type: task_type }));
});