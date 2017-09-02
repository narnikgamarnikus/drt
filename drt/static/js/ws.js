    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    socket = new WebSocket(ws_scheme + "://" + window.location.host + "/tables/");

    socket.onmessage = function(e) {
      

      $('#table').remove()
      $('#container-table').append('<table class="table table-bordered" id="table"></table>')

      matrix = JSON.parse(e.data).matrix
      var top_tr = '<tr id="top_tr"></tr>'
      var red_td = '<td style="background-color: red"></td>'      
      $('#table').append(top_tr)
      $('#top_tr').append(red_td)
      for (m in matrix) {
        $('#top_tr').append('<td>' + m + '</td>')
      }
      for (m in matrix) {
        $('#table').append('<tr id=' + m + '></tr>')
        $('#' + m).append('<td>' + m + '</td>')
        for (z in matrix[m]) {
          if (z == m) {
            $('#' + m).append(red_td)  
          } else {
          $('#' + m).append('<td>' + matrix[m][z] + '</td>')
          }
        }
      }
    }

    socket.onopen = function() {
      socket.send("connect");
    }

    socket.onclose = function() {
      socket.send("disconnect");   
    }

    if (socket.readyState == WebSocket.OPEN) socket.onopen();