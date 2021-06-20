#!/usr/bin/python
from redBlocks import *
from redBlocksTest import *

# This script was generated by the redBlocks Simulator's test script recorder.
# It serves for demonstration purposes and tests the application's behaviour when the vending machine's door is opened in order to do maintenance and fill up the slots.
# It needs to be started with the first slot being blocked and will end with all slots being unblocked.

scf = SimulatorConnectionFactory()

# Registration of interfaces
scf.registerDO("Product 4 Lamp")
scf.registerDO("Product 3 Lamp")
scf.registerDO("Product 2 Lamp")
scf.registerDO("Product 1 Lamp")
scf.registerDO("Dispense Bay Lamp")
scf.registerDO("Change Bay Lamp")
scf.registerDO("Open Cash Box Actor")
scf.registerDO("Cash Box Return Actor")
scf.registerDO("Product 1 Release Gear")
scf.registerDO("Product 2 Release Gear")
scf.registerDO("Product 3 Release Gear")
scf.registerDO("Product 4 Release Gear")
scf.registerCC("GSM Modem")
scf.registerDP("Display")
scf.registerDI("Product 4 Button")
scf.registerDI("Return Money Button")
scf.registerDI("Front Door Protection")
scf.registerSBO("KeyPad1")
scf.registerSBO("KeyPad2")
scf.registerSBO("KeyPad3")
scf.registerSBO("KeyPad4")
scf.registerDI("Filled Up Button")
sc = scf.create()

# Define set of interfaces to observe
observer = Observer()
observer.add(sc.DO("Product 4 Lamp"))
observer.add(sc.DO("Product 3 Lamp"))
observer.add(sc.DO("Product 2 Lamp"))
observer.add(sc.DO("Product 1 Lamp"))
observer.add(sc.DO("Dispense Bay Lamp"))
observer.add(sc.DO("Change Bay Lamp"))
observer.add(sc.DO("Open Cash Box Actor"))
observer.add(sc.DO("Cash Box Return Actor"))
observer.add(sc.DO("Product 1 Release Gear"))
observer.add(sc.DO("Product 2 Release Gear"))
observer.add(sc.DO("Product 3 Release Gear"))
observer.add(sc.DO("Product 4 Release Gear"))
observer.add(sc.CC("GSM Modem"), 0.10)
observer.add(sc.DP("Display"), 0.10)

# time tolerance: adjust to a suitable value depending on the latency of the test setup
TOL = 0.20
observer.setTolerance(TOL)

observer.start()
time = observer.getTime()


# Test Preconditions
observer[sc.DO("Product 4 Lamp")].checkData(False)
observer[sc.DO("Product 3 Lamp")].checkData(False)
observer[sc.DO("Product 2 Lamp")].checkData(False)
observer[sc.DO("Product 1 Lamp")].checkData(False)
observer[sc.DO("Dispense Bay Lamp")].checkData(False)
observer[sc.DO("Change Bay Lamp")].checkData(False)
observer[sc.DO("Open Cash Box Actor")].checkData(True)
observer[sc.DO("Cash Box Return Actor")].checkData(False)
observer[sc.DO("Product 1 Release Gear")].checkData(False)
observer[sc.DO("Product 2 Release Gear")].checkData(False)
observer[sc.DO("Product 3 Release Gear")].checkData(False)
observer[sc.DO("Product 4 Release Gear")].checkData(False)
observer[sc.DP("Display")].checkData(DisplayData.fromFileContents(binaryData('0.rbb')))

observer.sleep(0.253)

time = observer.getTime()
sc.DI("Product 4 Button").setValue(True)

observer[sc.DO("Product 4 Lamp")].addNoChangeCheck(time + 0.05 - TOL)
observer[sc.DO("Product 4 Lamp")].addEventCheck(time + 0.05 + TOL, True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.05 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.05 + TOL, DisplayData.fromFileContents(binaryData('1.rbb')))

observer.sleep(0.084)

time = observer.getTime()
sc.DI("Product 4 Button").setValue(False)

observer.sleep(1.018)

time = observer.getTime()
sc.DI("Return Money Button").setValue(True)

observer[sc.DO("Open Cash Box Actor")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DO("Open Cash Box Actor")].addEventCheck(time + 0.03 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 0.03 + TOL, True)

observer[sc.DO("Product 4 Lamp")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DO("Product 4 Lamp")].addEventCheck(time + 0.03 + TOL, False)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.03 + TOL, DisplayData.fromFileContents(binaryData('2.rbb')))

observer.sleep(0.083)

time = observer.getTime()
sc.DI("Return Money Button").setValue(False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 0.45 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 0.45 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 0.95 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 0.95 + TOL, True)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 1.53 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 1.53 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 1.95 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 1.95 + TOL, True)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 2.45 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 2.45 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 2.95 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 2.95 + TOL, True)

observer[sc.DP("Display")].addNoChangeCheck(time + 2.95 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 2.95 + TOL, DisplayData.fromFileContents(binaryData('0.rbb')))

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 3.45 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 3.45 + TOL, False)

observer.sleep(3.566)

time = observer.getTime()
sc.DI("Front Door Protection").setValue(False)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.03 + TOL, DisplayData.fromFileContents(binaryData('3.rbb')))

observer.sleep(1.571)

time = observer.getTime()
sc.SBO("KeyPad1").setValue(True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.05 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.05 + TOL, DisplayData.fromFileContents(binaryData('4.rbb')))

observer.sleep(0.363)

time = observer.getTime()
sc.SBO("KeyPad1").setValue(False)

observer.sleep(0.601)

time = observer.getTime()
sc.SBO("KeyPad2").setValue(True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.07 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.07 + TOL, DisplayData.fromFileContents(binaryData('5.rbb')))

observer.sleep(0.352)

time = observer.getTime()
sc.SBO("KeyPad2").setValue(False)

observer.sleep(0.702)

time = observer.getTime()
sc.SBO("KeyPad3").setValue(True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.07 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.07 + TOL, DisplayData.fromFileContents(binaryData('6.rbb')))

observer.sleep(0.316)

time = observer.getTime()
sc.SBO("KeyPad3").setValue(False)

observer.sleep(0.684)

time = observer.getTime()
sc.SBO("KeyPad4").setValue(True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.07 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.07 + TOL, DisplayData.fromFileContents(binaryData('7.rbb')))

observer.sleep(0.332)

time = observer.getTime()
sc.SBO("KeyPad4").setValue(False)

observer.sleep(0.838)

time = observer.getTime()
sc.DI("Filled Up Button").setValue(True)

observer.sleep(0.385)

time = observer.getTime()
sc.DI("Filled Up Button").setValue(False)

observer.sleep(1.502)

time = observer.getTime()
sc.DI("Front Door Protection").setValue(True)

observer[sc.DO("Open Cash Box Actor")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DO("Open Cash Box Actor")].addEventCheck(time + 0.03 + TOL, True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.03 + TOL, DisplayData.fromFileContents(binaryData('0.rbb')))

observer.sleep(1.217)

time = observer.getTime()
sc.DI("Product 4 Button").setValue(True)

observer[sc.DO("Product 4 Lamp")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DO("Product 4 Lamp")].addEventCheck(time + 0.03 + TOL, True)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.05 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.05 + TOL, DisplayData.fromFileContents(binaryData('8.rbb')))

observer.sleep(0.247)

time = observer.getTime()
sc.DI("Product 4 Button").setValue(False)

observer.sleep(1.038)

time = observer.getTime()
sc.DI("Return Money Button").setValue(True)

observer[sc.DO("Open Cash Box Actor")].addNoChangeCheck(time + 0.02 - TOL)
observer[sc.DO("Open Cash Box Actor")].addEventCheck(time + 0.02 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 0.02 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 0.02 + TOL, True)

observer[sc.DO("Product 4 Lamp")].addNoChangeCheck(time + 0.02 - TOL)
observer[sc.DO("Product 4 Lamp")].addEventCheck(time + 0.02 + TOL, False)

observer[sc.DP("Display")].addNoChangeCheck(time + 0.03 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 0.03 + TOL, DisplayData.fromFileContents(binaryData('2.rbb')))

observer.sleep(0.279)

time = observer.getTime()
sc.DI("Return Money Button").setValue(False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 0.25 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 0.25 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 0.75 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 0.75 + TOL, True)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 1.25 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 1.25 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 1.75 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 1.75 + TOL, True)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 2.25 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 2.25 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 2.75 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 2.75 + TOL, True)

observer[sc.DP("Display")].addNoChangeCheck(time + 2.75 - TOL)
observer[sc.DP("Display")].addEventCheck(time + 2.75 + TOL, DisplayData.fromFileContents(binaryData('0.rbb')))

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 3.26 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 3.26 + TOL, False)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 3.76 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 3.76 + TOL, True)

observer[sc.DO("Open Cash Box Actor")].addNoChangeCheck(time + 4.26 - TOL)
observer[sc.DO("Open Cash Box Actor")].addEventCheck(time + 4.26 + TOL, True)

observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time + 4.26 - TOL)
observer[sc.DO("Change Bay Lamp")].addEventCheck(time + 4.26 + TOL, False)

observer.sleep(5.141 + TOL)

time = observer.getTime()

# Test end conditions
observer[sc.DO("Product 4 Lamp")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 3 Lamp")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 2 Lamp")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 1 Lamp")].addNoChangeCheck(time - TOL)
observer[sc.DO("Dispense Bay Lamp")].addNoChangeCheck(time - TOL)
observer[sc.DO("Change Bay Lamp")].addNoChangeCheck(time - TOL)
observer[sc.DO("Open Cash Box Actor")].addNoChangeCheck(time - TOL)
observer[sc.DO("Cash Box Return Actor")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 1 Release Gear")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 2 Release Gear")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 3 Release Gear")].addNoChangeCheck(time - TOL)
observer[sc.DO("Product 4 Release Gear")].addNoChangeCheck(time - TOL)
observer[sc.CC("GSM Modem")].addNoChangeCheck(time - TOL)
observer[sc.DP("Display")].addNoChangeCheck(time - TOL, [0, 0, 128, 64])

observer.stop()