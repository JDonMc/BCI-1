
setup{
    runningcircuit.initialiseNeurons()
    runningcircuit.activate("initial")
}

mainloop{

    timer = time.currenttime()

    runningcircuit.switchOn()
    #refers to below code
    switchOn (){
    #will need to include data from a file, with a list of "cases" which are possible outputs of each neural network
    #only enabled once trained X times (where X achieves a high rate of accuracy, ie. 95% ie. 20 datapoints
    switch(runningcircuit.activated()):
        case "initial":
        switch(runningcircuit.output()):
            case "trigger"
            runningcircuit.activate("triggered") #could include a wait + switchOn sequence
            break;
            break;
            case "standby"
            waitforphysicalactivation(pinX, High/low - pullup pulldown button) #sleep til interrupt
            break;
            break;
        case "triggered":
        switch(runningcircuit.output()):
            case "phone"
            runningcircuit.activate("triggered phone")
            break;
            case "computer"
            runningcircuit.activate("triggered computer")
            break;
            case "homebot"
            runningcircuit.activate("triggered homebot")
            break;
            case "quadcopter"
            runningcircuit.activate("triggered quadcopter")
            break;


        case "triggered phone":
        switch(runningcircuit.output()):
            case "call"
            runningcircuit.activate("triggered phone call")
            break;
            case "text"
            runningcircuit.activate("triggered phone text")
            break;

        #do stuff

        case "triggered computer":
        switch(runningcircuit.output()):
            case "run"
            runningcircuit.activate("triggered computer run")
            break;
            case "open"
            case "send"
            case "note"

        #do stuff

        case "triggered homebot":

        case "triggered quadcopter":
        switch(runningcircuit.output()):
            case "triggered quadcopter specific"
            runningcircuit.activate("specific")
            break;
            case "abstract"
            runningcircuit.activate("")

    }

    if(runningcircuit.recentsuccessfulsequence() == True):
        runningcircuit.applyrecentlearning() #change recent successful sequence to False

    totalwait = 500 #500 ms
    waitremain = totalwait - (time.currenttime() - timer)
    if (waitremain > 0):
        wait(waitremain)

}