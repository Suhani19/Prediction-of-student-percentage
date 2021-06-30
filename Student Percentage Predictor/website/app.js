function predictPercentage() {
  var study_hours = document.getElementById("study_hours");
  var percentage_scores = document.getElementById("percentage_scores");

  var url = "http://127.0.0.1:5000/predict_score";

 

  $.post(url, {
    study_hours: parseFloat(study_hours.value),
  },function(data, status) {
   
      if(data.predicted_score>100){
        data.predicted_score=99.99;
      }
      percentage_scores.innerHTML = "<div class='result'>"+ data.predicted_score + "%" + "</div>";
      console.log(status);
  });
}