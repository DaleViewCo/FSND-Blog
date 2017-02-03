function addLike(post_id){
	$.ajax({
		type: 'post',
		contentType: 'application/json',
		dataType: 'json',
		data: JSON.stringify({
			'pid': post_id,
			'type': "Like"
		}),
		success: function(response){
			$("div#like-count").html('');
			$("div#like-count").html(response.data);
		},
		error: function(request, status, error){
			alert(response);
		}
	})
}