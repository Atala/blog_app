

function show_months()
{if(!($("#left > li > ul > li").is(':visible'))){
	$("#left > li > ul > li").show(); }
else{
	$("#left > li > ul > li").hide();
}

}

function hide_months()
{
$("#left > li > ul > li").hide();
}