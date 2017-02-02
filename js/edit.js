function editPost(post_id){
	var post_content = $("textarea#post-content").val();
	var subject = $("textarea#post-subject").val();
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'subject': subject,
			'post': post_content
		}),
		success: function(){
			window.location.replace('/blog/'+ post_id);
		}
	})
}

function cancelEditPost(post_id){
	window.location.replace('/blog/'+ post_id);
}

function deletePost(post_id){
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'pid': post_id,
			'type': "DeletePost"
		}),
		success: function(response){
			window.location.replace('/login');
		}
	})
}