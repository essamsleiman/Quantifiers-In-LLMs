// This is gptmodel on first question

var total = 30;

var statePrior = function () {
  return uniformDraw(_.range(total + 1));
};

var uttFreq = [0.01, 0.47, 0.19, 0.29, 0.01, 0.01, 0.01, 0.01];

var utterances = [
  "a_couple",
  "a_few",
  "some",
  "several",
  "most",
  "a_majority",
  "almost_all",
  "all",
];

var utterancePrior = function () {
  categorical({ ps: uttFreq, vs: utterances });
};

var bounds = {
  all: [28, total],
  almost_all: [25, 29],
  a_majority: [20, total],
  most: [22, total],
  several: [5, 13],
  some: [4, 10],
  a_few: [0, 10],
  a_couple: [0, 14],
};

// meaning function to interpret the utterances
var literalMeanings = function (utt, state) {
  var interval = bounds[utt];
  return (state >= interval[0]) & (state <= interval[1]);
};

// literal listener
var literalListener = cache(function (utt) {
  return Infer({
    model: function () {
      var state = statePrior();
      condition(literalMeanings(utt, state));
      return state;
    },
  });
});

var weber_fraction = 0.1;

// returns a state which is perceived when the true state is 'true_state'
var ANS = cache(function (true_state) {
  var true_state = Math.max(true_state, 0.01);
  Infer({
    method: "enumerate",
    model: function () {
      var perceived_state = uniformDraw(_.range(total + 1));
      factor(
        Gaussian({ mu: true_state, sigma: weber_fraction * true_state }).score(
          perceived_state
        )
      );
      return perceived_state;
    },
  });
});

var perceivedState = cache(function (true_state) {
  Infer({
    method: "enumerate",
    model: function () {
      var perceived_state = uniformDraw(_.range(total + 1));
      factor(ANS(true_state).score(perceived_state));
      factor(ANS(total - true_state).score(total - perceived_state));
      return perceived_state;
    },
  });
});

// set speaker optimality
var alpha = 1;

// pragmatic speaker
var speaker = cache(function (state) {
  return Infer({
    model: function () {
      var utt = utterancePrior();
      var perceived_state = sample(perceivedState(state));
      factor(alpha * literalListener(utt).score(perceived_state));
      return utt;
    },
  });
});

// pragmatic listener
var pragmaticListener = cache(function (utt) {
  return Infer({
    model: function () {
      var state = statePrior();
      observe(speaker(state), utt);
      return state;
    },
  });
});

var value = 5;
viz(speaker(value));
// viz.density(pragmaticListener("a_few"))
var speakerDist = speaker(value);
console.log(speakerDist);
