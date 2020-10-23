#   Data Set  for tests Description

       data-test1.csv: Step number increases from 0 to 1200 in 10 minutes
       Result: 1 walking event incremented and 10 minutes walking time incremented

       data-test2.csv: Step number increases from 0 to 1199 in 10 minutes
       Result: 0 walking event incremented and 0 minutes walking time incremented

       data-test3.csv: Step number increases from 0 to 1205 in 10 minutes
       Result: 1 walking event incremented and 10 minutes walking time incremented

       data-test4.csv: Step number increases from 0 to 1200 in 10 minutes
       The step counter has variable velocity
       Result: 1 walking event incremented and 10 minutes walking time incremented

       data-test5.csv: Step number increases from 0 to 1199 in 10 minutes
       The step counter has variable velocity
       Result: 0 walking event incremented and 0 minutes walking time incremented

       Gap of instant reset: Problem that must be solved throgh data processing
       or designing the project so that the device send the instant time of the
       reset.

       data-test6.csv: Step number increases from 0 to 1200 in 10 minutes
       In this case the user maintain a uniform velocity, but he resets
       the device (lim t -> 0-) seconds before data be sent. So
       the reseted step number will be sent and the devices will lose
       (lim steps -> 60) steps. ERROR: Almost 60 steps
       Result: 0 walking event incremented and 0 minutes walking time incremented

       data-test7.csv: Step number increases from 0 to 1200 in 10 minutes
       In this case the user maintain a uniform velocity, but he resets
       the device (lim t -> 0+) seconds after data be sent. So
       the step number will be sent and the devices will lose
       (lim steps -> 0) steps. ERROR: Almost 0 steps
       Result: 1 walking event incremented and 10 minutes walking time incremented

       data-test8.csv: For tests for reset
           Test 1: Step number increases 1200 in 10 minutes
           considering 1 reset event in first walking.

           Test 2: Step number increases 1200 in 10 minutes and there
           are 3 reset in walking time
           OBS: it's considered that between a data transfer interval
           there's no more than 1 reset event

       Problems:
           Test 3: Step number is 300 for 4 measures in 10 minutes and it's
           a problem if the user click on reset even after he send data
           and before he complete the first pass. The ideal result would
           be 1 walking and 10 minutes walked, but the real result is 0
           walkings and 0 minute walked
           OBS: t's considered that between a data transfer interval
           there's no more than 1 reset event

           test 4: Here we ca have the same problem of the test 3, but
           apparently we have step velocity, but it's not enough to complete a
           walking. However, if we have resets before send data, there's data
           inconsistence.


       If we have 2 resets between step number data being sent, we have inconsistence

       Result: 2 walking event incremented and 2 minutes walking time incremented.

       Mathematically there are three possibilities where the the step speed
       can be infinite.
           * If there are no connection (t2 - t1) -> infinite
           * If there velocity of the user v -> infinite 
           * If the user resets the step counter device lim t -> 0
           before a step be completed.

       Other tests:

       data-test8.csv: Step number increases from 0 to 1199 in 10 minutes
       Result: 3 walking event incremented and 3 minutes walking time incremented

       data-test3.csv: Step number increases from 0 to 1205 in 10 minutes
       Result: 1 walking event incremented and 10 minutes walking time incremented

       data-test4.csv: Step number increases from 0 to 1200 in 10 minutes
       The step counter has variable velocity
       Result: 1 walking event incremented and 10 minutes walking time incremented

       data-test5.csv: Step number increases from 0 to 1199 in 10 minutes
       The step counter has variable velocity
       Result: 0 walking event incremented and 0 minutes walking time incremented