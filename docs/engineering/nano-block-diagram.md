# Nano Rev A functional block diagram (unvalidated)

```text
     Protected DC input
             |
    power supervisor / PMIC
      |       |        |
   SoC core  DDR     peripherals
      |       |        |
      +---- bare ARM64 SoC ---- DDR RAM
                |    |     |
               eMMC UART  Ethernet MAC
                            |
                          PHY + magnetics
                            |
                           RJ45

 Independent always-on management MCU
    |      |         |         |
   rail   reset    watchdog   telemetry
 control  request   heartbeat  fault log
```

All arrows and blocks are logical only, not electrical connections or finalized architecture. Rail sequencing, MCU/host reset isolation, power switching, clock source, boot strap selection and GPIO electrical levels depend on selected SoC.

## Schematic sheet plan
1. Hierarchy, power entry and protection
2. SoC, clocks, straps and boot modes
3. DDR memory and termination
4. PMIC and sequencing
5. eMMC / recovery / UART
6. Ethernet PHY, magnetics, ESD and RJ45
7. Management MCU, programming and watchdog
8. Board identification, connectors, test points and mechanical

## PCB review before layout
Obtain fabricator-approved stackup; document DDR trace matching and return paths, controlled impedance, vias/escape routing, BGA assembly capability, ESD/EMC grounding and thermal copper strategy. Do not start routing from generic internet rules of thumb.
