function postComment(post_id){
	var content = $("#comment-text-area-id").val().trim();
	if(content == ''){
		return;
	}
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'comment': content,
			'pid': post_id,
			'type': "NewComment"
		}),
		success: function(response){
			var newHTML = $("div#comment-content-id").html();
			var comment_id = response.id;
			var functionText = 'editComment(' + comment_id + ')';

			newHTML += response.data;
			newHTML +='<a class="link" onclick="' + functionText + '>Edit</a>';

			$("div#comment-content-id").html(newHTML);
			$("textarea#comment-text-area-id").val('');
		},
		error: function(request, status, error){
			alert("Error"+request.responseText);
		}
	})
}

function editComment(comment_id, post_id){
	var existing = $("p#" + comment_id).text().trim();
	var edit_area = $("<textarea id=" +comment_id+" class='edit-comment-text'" +
		"onkeypress = 'submitEdit(event, "+comment_id+", "+ post_id+")'/>");
	edit_area.val(existing);
	$("p#" + comment_id).replaceWith(edit_area);
}

function submitEdit(event, comment_id, post_id){
	if(event.which == 13){
		var new_text = $("textarea#" + comment_id).val().trim();
		$.ajax({
			type: 'post',
			contentType: 'application/json',
			dataType: 'json',
			data: JSON.stringify({
				'pid': post_id,
				'comment-id': comment_id,
				'edited-comment': new_text,
				'type': "EditComment"
			}),
			success: function(response){
				var new_comment = $("<p id="+comment_id+" class=comment-text/>");
				new_comment.text(new_text);
				$("textarea#"+comment_id).replaceWith(new_comment);
			},
			error: function(response){
				alert("Error");
			}
		})
	}
}

function deleteComment(comment_id, post_id){
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'type': "DeleteComment",
			'comment-id': comment_id,
			'pid': post_id
		}),
		success: function(response){
			$("p#"+comment_id).remove();
			$("a#edit-"+comment_id).remove();
			$("a#delete-"+comment_id).remove();
		},
		error: function(reponse){
			alert("Delete Error");
		}
	})
}