
if (document.getElementById("state1")) {
    const countUp = new CountUp(
      "state1",
      document.getElementById("state1").getAttribute("countTo")
    );
    if (!countUp.error) {
      countUp.start();
    } else {
      console.error(countUp.error);
    }
  }
  if (document.getElementById("state2")) {
    const countUp = new CountUp(
      "state2",
      document.getElementById("state2").getAttribute("countTo")
    );
    if (!countUp.error) {
      countUp.start();
    } else {
      console.error(countUp.error);
    }
  }
  if (document.getElementById("state3")) {
    const countUp = new CountUp(
      "state3",
      document.getElementById("state3").getAttribute("countTo")
    );
    if (!countUp.error) {
      countUp.start();
    } else {
      console.error(countUp.error);
    }
  }
  if (document.getElementById("state4")) {
    const countUp = new CountUp(
      "state4",
      document.getElementById("state4").getAttribute("countTo")
    );
    if (!countUp.error) {
      countUp.start();
    } else {
      console.error(countUp.error);
    }
  }