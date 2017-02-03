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
		},
		error: function(){
			cancelEditPost(post_id);
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
			// remove the entire permalink content and replace with
			// empty

			var new_html = '<div class="container">'+
			'<div class="row">'+
			'<div class="col-sm-10">'+
			'<h1 class="main-title"><a href="/blog" class="main-title">FSND Blog</a></h1>'+
			'</div>'+
			'<div class="col-sm-2">'+
			'<a class="logout" href="/logout">Logout</a>'+
			'</div>'+
			'</div>'+
			'<div class="row">'+
			'<div class="col-sm-12"><hr></div>'+
			'</div>'+
			'</div>';

			$("div#permalink").replaceWith(new_html);
			// window.location.replace('/blog');
		}
	})
}