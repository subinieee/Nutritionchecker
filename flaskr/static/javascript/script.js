function addRow() {
    var myName = document.getElementById("name");
    var age = document.getElementById("age");
    var table = document.getElementById("myTableData");

    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);

    row.insertCell(0).innerHTML= myName.value;
    row.insertCell(1).innerHTML= age.value;
    row.insertcell(2).innerHTML='<input type="button" value = "Delete" onClick="Javacsript:deleteRow(this)">';}

function deleteRow(obj) {

    var index = obj.parentNode.parentNode.rowIndex;
    var table = document.getElementById("myTableData");
    table.deleteRow(index);

}

function addTable() {

    var myTableDiv = document.getElementById("myDynamicTable");

    var table = document.createElement('TABLE');
    table.border='1';

    var tableBody = document.createElement('TBODY');
    table.appendChild(tableBody);

    for (var i=0; i<3; i++){
       var tr = document.createElement('TR');
       tableBody.appendChild(tr);

       for (var j=0; j<4; j++){
           var td = document.createElement('TD');
           td.width='75';
           td.appendChild(document.createTextNode("Cell " + i + "," + j));
           tr.appendChild(td);
       }
    }
    myTableDiv.appendChild(table);

}

function load() {

    console.log("Page load finished");

}

function arrangeSno()

    {
           var i=0;
            $('#pTable tr').each(function() {
                $(this).find(".sNo").html(i);
                i++;
             });

    }

$(document).ready(function(){
$('#addButId').click(function(){
                   var sno=$('#pTable tr').length;
                       trow=  "<tr><td class='sNo'>"+sno+"</td>"+
                           "<td><input name='FOOD' type='text'></td>"+
                           "<td><input name='Portion' type='text'></td>"+
                           "<td><select name='time'><option value='B'>Breakfast</option><option value='L'>Lunch</option><option value='D'>Dinner</option></select></td>"+
                          "<td><button type='button' class='rButton btn btn-sb'>Remove</button></td></tr>";
                      $('#pTable').append(trow);
                    });
                     });

$(document).on('click', 'button.rButton', function () {
       $(this).closest('tr').remove();
       arrangeSno();
     return false;
 });
