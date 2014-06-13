$(function() {
  $("a.download").click(function() {
    $("a.download").prop('disabled', true);
    $("a.download").removeClass("go").addClass("processing");
    $("a.download").removeClass("btn-success").addClass("btn-warning");
  })
});
