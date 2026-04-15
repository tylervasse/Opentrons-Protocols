import json
from opentrons import protocol_api, types

metadata = {
    "protocolName": "103025 1 Joy Combined RTPCR TVasse 6samps (2 Proprietary Primers)",
    "author": "Tyler Vasse",
    "created": "2025-04-07T18:15:01.428Z",
    "lastModified": "2025-10-30T18:02:54.561Z",
    "protocolDesigner": "8.6.2",
    "source": "Protocol Designer",
}

requirements = {"robotType": "OT-2", "apiLevel": "2.26"}

def run(protocol: protocol_api.ProtocolContext) -> None:
    # Load Labware:
    tip_rack_1 = protocol.load_labware(
        "opentrons_96_filtertiprack_200ul",
        location="9",
        namespace="opentrons",
        version=1,
    )
    tip_rack_2 = protocol.load_labware(
        "opentrons_96_filtertiprack_20ul",
        location="8",
        namespace="opentrons",
        version=1,
    )
    tube_rack_1 = protocol.load_labware(
        "opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap",
        location="5",
        namespace="opentrons",
        version=2,
    )
    well_plate_1 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/individualpcrtubes_96_wellplate_200ul/1"],
        location="1",
    )
    tube_rack_2 = protocol.load_labware_from_definition(
        CUSTOM_LABWARE["custom_beta/opentrons_24_tall_tubes/1"],
        location="4",
    )
    well_plate_2 = protocol.load_labware(
        "biorad_96_wellplate_200ul_pcr",
        location="2",
        namespace="opentrons",
        version=4,
    )

    # Load Pipettes:
    pipette_left = protocol.load_instrument("p300_single_gen2", "left")
    pipette_right = protocol.load_instrument("p20_single_gen2", "right")

    # Define Liquids:
    liquid_1 = protocol.define_liquid(
        "5x miRCURY",
        display_color="#51ff4fff",
    )
    liquid_2 = protocol.define_liquid(
        "PCR Grade Water",
        display_color="#0700ffff",
    )
    liquid_3 = protocol.define_liquid(
        "10x miRCURY",
        display_color="#fb1f0eff",
    )
    liquid_4 = protocol.define_liquid(
        "Uni-Sp6",
        display_color="#efff01ff",
    )
    liquid_5 = protocol.define_liquid(
        "miRNA 100uM",
        display_color="#50d5ff",
    )
    liquid_6 = protocol.define_liquid(
        "2x miRCURY",
        display_color="#fe1414ff",
    )
    liquid_7 = protocol.define_liquid(
        "U6 primer mix",
        display_color="#edd511ff",
    )
    liquid_8 = protocol.define_liquid(
        "primer mix 2",
        display_color="#389be6ff",
    )
    liquid_9 = protocol.define_liquid(
        "Sample",
        display_color="#9dffd8ff",
    )
    liquid_10 = protocol.define_liquid(
        "gDNA Wipeout Buffer 7x",
        display_color="#00d3ffff",
    )
    liquid_11 = protocol.define_liquid(
        "Quantiscript Reverse Transcriptase",
        display_color="#ff5000ff",
    )
    liquid_12 = protocol.define_liquid(
        "RT Buffer",
        display_color="#ac00ffff",
    )
    liquid_13 = protocol.define_liquid(
        "RT Primer Mix",
        display_color="#ffc500ff",
    )
    liquid_14 = protocol.define_liquid(
        "2x QuantiNOVA SYBR Green PCR MM",
        display_color="#12ed11ff",
    )
    liquid_15 = protocol.define_liquid(
        "Proprietary Primers",
        display_color="#fff442ff",
    )
    liquid_16 = protocol.define_liquid(
        "IDT primers",
        display_color="#9dffd8ff",
    )
    liquid_17 = protocol.define_liquid(
        "10uM Primer",
        display_color="#9dffd8ff",
    )

    # Load Liquids:
    tube_rack_2.load_liquid(
        wells=["A1"],
        liquid=liquid_10,
        volume=100,
    )
    tube_rack_2.load_liquid(
        wells=["A2"],
        liquid=liquid_2,
        volume=1000,
    )
    tube_rack_2.load_liquid(
        wells=["A3"],
        liquid=liquid_11,
        volume=100,
    )
    tube_rack_2.load_liquid(
        wells=["A4"],
        liquid=liquid_12,
        volume=100,
    )
    tube_rack_2.load_liquid(
        wells=["A6"],
        liquid=liquid_14,
        volume=1000,
    )
    tube_rack_2.load_liquid(
        wells=["B1", "B2"],
        liquid=liquid_15,
        volume=1000,
    )
    well_plate_1.load_liquid(
        wells=["D1", "D2", "D3", "D4", "D5", "D6"],
        liquid=liquid_9,
        volume=10,
    )

    # PROTOCOL STEPS

    # Step 1: 16uL GDNA Wipeout Master Mix
    pipette_right.transfer_with_liquid_class(
        volume=16,
        source=[tube_rack_2["A1"]],
        dest=[tube_rack_1["A1"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_1",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 2: 88uL RNAse Free Water
    pipette_left.transfer_with_liquid_class(
        volume=88,
        source=[tube_rack_2["A2"]],
        dest=[tube_rack_1["A1"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_2",
            properties={"p300_single_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 35},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 3: 13uL MM into each PCR tube
    pipette_right.transfer_with_liquid_class(
        volume=13,
        source=[tube_rack_1["A1"], tube_rack_1["A1"], tube_rack_1["A1"], tube_rack_1["A1"], tube_rack_1["A1"], tube_rack_1["A1"]],
        dest=[well_plate_1["G1"], well_plate_1["G2"], well_plate_1["G3"], well_plate_1["G4"], well_plate_1["G5"], well_plate_1["G6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_3",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 4: 1uL of Samp
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["D1"], well_plate_1["D2"], well_plate_1["D3"], well_plate_1["D4"], well_plate_1["D5"], well_plate_1["D6"]],
        dest=[well_plate_1["G1"], well_plate_1["G2"], well_plate_1["G3"], well_plate_1["G4"], well_plate_1["G5"], well_plate_1["G6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_4",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": True, "duration": 3},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 2, "volume": 10},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 5: pause
    protocol.pause("Place PCR tubes with gDNA and sample mixtures onto the 42C heat block for 2 minutes and then place on ice. In the meantime, start the next portion of the protocol.")

    # Step 6: 8uL RTase
    pipette_right.transfer_with_liquid_class(
        volume=8,
        source=[tube_rack_2["A3"]],
        dest=[tube_rack_1["A2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_6",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 3.7)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 7: 40uL Premix RT Buffer + RT Primer
    pipette_left.transfer_with_liquid_class(
        volume=40,
        source=[tube_rack_2["A4"]],
        dest=[tube_rack_1["A2"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_7",
            properties={"p300_single_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 46.4)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 46.43)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 8: Mixing RT MM
    pipette_left.pick_up_tip(location=tip_rack_1)
    pipette_left.mix(
        repetitions=10,
        volume=35,
        location=tube_rack_1["A2"].bottom(z=1.5),
        aspirate_flow_rate=46.4,
        dispense_flow_rate=46.43,
        final_push_out=0,
    )
    pipette_left.drop_tip()

    # Step 9: pause
    protocol.pause("Remove PCR tubes from ice and place into individual PCR plate holder.")

    # Step 10: 6uL RT MM into gDNA Wipeout
    pipette_right.transfer_with_liquid_class(
        volume=6,
        source=[tube_rack_1["A2"], tube_rack_1["A2"], tube_rack_1["A2"], tube_rack_1["A2"], tube_rack_1["A2"], tube_rack_1["A2"]],
        dest=[well_plate_1["G1"], well_plate_1["G2"], well_plate_1["G3"], well_plate_1["G4"], well_plate_1["G5"], well_plate_1["G6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_10",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 20)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 10},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 6, "volume": 15},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 11: pause
    protocol.pause("Place PCR tubes with RTase and sample mixture on the 42C heatblock for 15 minutes and then place on the 95C heatblock for 3 minutes, and then place on ice. Remove gDNA wipeout (A1), RTase (A3), Premix RT (A4) and place into freezer. Once ready, load primers into machine.")

    # Step 12: 240uL 2x SYBR Green MM
    pipette_left.transfer_with_liquid_class(
        volume=240,
        source=[tube_rack_2["A6"], tube_rack_2["A6"]],
        dest=[tube_rack_1["A3"], tube_rack_1["A4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_12",
            properties={"p300_single_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 77)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 200)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 13: 48uL Proprietary Forward Primer
    pipette_left.transfer_with_liquid_class(
        volume=48,
        source=[tube_rack_2["B1"], tube_rack_2["B2"]],
        dest=[tube_rack_1["A3"], tube_rack_1["A4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_13",
            properties={"p300_single_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 46.4)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 46.4)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 2, "volume": 40},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 14: 168uL RNAse Free H2O
    pipette_left.transfer_with_liquid_class(
        volume=168,
        source=[tube_rack_2["A2"], tube_rack_2["A2"]],
        dest=[tube_rack_1["A3"], tube_rack_1["A4"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_1],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_14",
            properties={"p300_single_gen2": {"opentrons/opentrons_96_filtertiprack_200ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 2.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 250)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 3},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 250)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {
                            "enabled": True,
                            "location": "destination",
                            "flow_rate": 46.43,
                        },
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 10, "volume": 100},
                },
            }}},
        ),
    )
    pipette_left.drop_tip()

    # Step 15: 19uL PCR 1 MM
    pipette_right.transfer_with_liquid_class(
        volume=19,
        source=[tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"], tube_rack_1["A3"]],
        dest=[well_plate_2["A1"], well_plate_2["B1"], well_plate_2["C1"], well_plate_2["D1"], well_plate_2["E1"], well_plate_2["F1"], well_plate_2["A2"], well_plate_2["B2"], well_plate_2["C2"], well_plate_2["D2"], well_plate_2["E2"], well_plate_2["F2"], well_plate_2["A3"], well_plate_2["B3"], well_plate_2["C3"], well_plate_2["D3"], well_plate_2["E3"], well_plate_2["F3"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_15",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 12)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 12)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 16: 19uL PCR 2 MM
    pipette_right.transfer_with_liquid_class(
        volume=19,
        source=[tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"], tube_rack_1["A4"]],
        dest=[well_plate_2["A4"], well_plate_2["B4"], well_plate_2["C4"], well_plate_2["D4"], well_plate_2["E4"], well_plate_2["F4"], well_plate_2["A5"], well_plate_2["B5"], well_plate_2["C5"], well_plate_2["D5"], well_plate_2["E5"], well_plate_2["F5"], well_plate_2["A6"], well_plate_2["B6"], well_plate_2["C6"], well_plate_2["D6"], well_plate_2["E6"], well_plate_2["F6"]],
        new_tip="once",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_16",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1.5},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 12)],
                    "pre_wet": False,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 12)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": False},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": False},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 17: 1uL cDNA Samps
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["G1"], well_plate_1["G1"], well_plate_1["G1"], well_plate_1["G1"], well_plate_1["G1"], well_plate_1["G1"]],
        dest=[well_plate_2["A1"], well_plate_2["A2"], well_plate_2["A3"], well_plate_2["A4"], well_plate_2["A5"], well_plate_2["A6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_17",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 6)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 18: 1uL cDNA Samps
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["G2"], well_plate_1["G2"], well_plate_1["G2"], well_plate_1["G2"], well_plate_1["G2"], well_plate_1["G2"]],
        dest=[well_plate_2["B1"], well_plate_2["B2"], well_plate_2["B3"], well_plate_2["B4"], well_plate_2["B5"], well_plate_2["B6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_18",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 6)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 19: 1uL cDNA Samps
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["G3"], well_plate_1["G3"], well_plate_1["G3"], well_plate_1["G3"], well_plate_1["G3"], well_plate_1["G3"]],
        dest=[well_plate_2["C1"], well_plate_2["C2"], well_plate_2["C3"], well_plate_2["C4"], well_plate_2["C5"], well_plate_2["C6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_19",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 6)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 20: 1uL cDNA Samps
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["G4"], well_plate_1["G4"], well_plate_1["G4"], well_plate_1["G4"], well_plate_1["G4"], well_plate_1["G4"]],
        dest=[well_plate_2["D1"], well_plate_2["D2"], well_plate_2["D3"], well_plate_2["D4"], well_plate_2["D5"], well_plate_2["D6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_20",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 6)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 21: 1uL cDNA Samps
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["G5"], well_plate_1["G5"], well_plate_1["G5"], well_plate_1["G5"], well_plate_1["G5"], well_plate_1["G5"]],
        dest=[well_plate_2["E1"], well_plate_2["E2"], well_plate_2["E3"], well_plate_2["E4"], well_plate_2["E5"], well_plate_2["E6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_21",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 6)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

    # Step 22: 1uL cDNA Samps
    pipette_right.transfer_with_liquid_class(
        volume=1,
        source=[well_plate_1["G6"], well_plate_1["G6"], well_plate_1["G6"], well_plate_1["G6"], well_plate_1["G6"], well_plate_1["G6"]],
        dest=[well_plate_2["F1"], well_plate_2["F2"], well_plate_2["F3"], well_plate_2["F4"], well_plate_2["F5"], well_plate_2["F6"]],
        new_tip="always",
        trash_location=protocol.fixed_trash,
        keep_last_tip=True,
        tip_racks=[tip_rack_2],
        liquid_class=protocol.define_liquid_class(
            name="transfer_step_22",
            properties={"p20_single_gen2": {"opentrons/opentrons_96_filtertiprack_20ul/1": {
                "aspirate": {
                    "aspirate_position": {
                        "offset": {"x": 0, "y": 0, "z": 1},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 6)],
                    "pre_wet": True,
                    "correction_by_volume": [(0, 0)],
                    "delay": {"enabled": False},
                    "mix": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                    },
                },
                "dispense": {
                    "dispense_position": {
                        "offset": {"x": 0, "y": 0, "z": 0.2},
                        "position_reference": "well-bottom",
                    },
                    "flow_rate_by_volume": [(0, 10)],
                    "delay": {"enabled": False},
                    "submerge": {
                        "delay": {"enabled": False},
                        "speed": 125,
                        "start_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                    },
                    "retract": {
                        "air_gap_by_volume": [(0, 0)],
                        "delay": {"enabled": False},
                        "end_position": {
                            "offset": {"x": 0, "y": 0, "z": 2},
                            "position_reference": "well-top",
                        },
                        "speed": 125,
                        "touch_tip": {"enabled": False},
                        "blowout": {"enabled": True, "location": "destination", "flow_rate": 3.78},
                    },
                    "correction_by_volume": [(0, 0)],
                    "push_out_by_volume": [(0, 0)],
                    "mix": {"enabled": True, "repetitions": 3, "volume": 8},
                },
            }}},
        ),
    )
    pipette_right.drop_tip()

CUSTOM_LABWARE = json.loads("""{"custom_beta/individualpcrtubes_96_wellplate_200ul/1":{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Individual PCR Tubes","brandId":[]},"metadata":{"displayName":"Individual PCR Tubes 96 Well Plate 200 µL","displayCategory":"wellPlate","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.76,"yDimension":85.48,"zDimension":21.06},"wells":{"A1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":74.24,"z":1.06},"B1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":65.24,"z":1.06},"C1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":56.24,"z":1.06},"D1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":47.24,"z":1.06},"E1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":38.24,"z":1.06},"F1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":29.24,"z":1.06},"G1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":20.24,"z":1.06},"H1":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":14.38,"y":11.24,"z":1.06},"A2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":74.24,"z":1.06},"B2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":65.24,"z":1.06},"C2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":56.24,"z":1.06},"D2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":47.24,"z":1.06},"E2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":38.24,"z":1.06},"F2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":29.24,"z":1.06},"G2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":20.24,"z":1.06},"H2":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":23.38,"y":11.24,"z":1.06},"A3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":74.24,"z":1.06},"B3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":65.24,"z":1.06},"C3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":56.24,"z":1.06},"D3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":47.24,"z":1.06},"E3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":38.24,"z":1.06},"F3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":29.24,"z":1.06},"G3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":20.24,"z":1.06},"H3":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":32.38,"y":11.24,"z":1.06},"A4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":74.24,"z":1.06},"B4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":65.24,"z":1.06},"C4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":56.24,"z":1.06},"D4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":47.24,"z":1.06},"E4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":38.24,"z":1.06},"F4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":29.24,"z":1.06},"G4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":20.24,"z":1.06},"H4":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":41.38,"y":11.24,"z":1.06},"A5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":74.24,"z":1.06},"B5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":65.24,"z":1.06},"C5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":56.24,"z":1.06},"D5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":47.24,"z":1.06},"E5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":38.24,"z":1.06},"F5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":29.24,"z":1.06},"G5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":20.24,"z":1.06},"H5":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":50.38,"y":11.24,"z":1.06},"A6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":74.24,"z":1.06},"B6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":65.24,"z":1.06},"C6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":56.24,"z":1.06},"D6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":47.24,"z":1.06},"E6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":38.24,"z":1.06},"F6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":29.24,"z":1.06},"G6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":20.24,"z":1.06},"H6":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":59.38,"y":11.24,"z":1.06},"A7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":74.24,"z":1.06},"B7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":65.24,"z":1.06},"C7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":56.24,"z":1.06},"D7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":47.24,"z":1.06},"E7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":38.24,"z":1.06},"F7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":29.24,"z":1.06},"G7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":20.24,"z":1.06},"H7":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":68.38,"y":11.24,"z":1.06},"A8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":74.24,"z":1.06},"B8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":65.24,"z":1.06},"C8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":56.24,"z":1.06},"D8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":47.24,"z":1.06},"E8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":38.24,"z":1.06},"F8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":29.24,"z":1.06},"G8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":20.24,"z":1.06},"H8":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":77.38,"y":11.24,"z":1.06},"A9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":74.24,"z":1.06},"B9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":65.24,"z":1.06},"C9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":56.24,"z":1.06},"D9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":47.24,"z":1.06},"E9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":38.24,"z":1.06},"F9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":29.24,"z":1.06},"G9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":20.24,"z":1.06},"H9":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":86.38,"y":11.24,"z":1.06},"A10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":74.24,"z":1.06},"B10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":65.24,"z":1.06},"C10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":56.24,"z":1.06},"D10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":47.24,"z":1.06},"E10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":38.24,"z":1.06},"F10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":29.24,"z":1.06},"G10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":20.24,"z":1.06},"H10":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":95.38,"y":11.24,"z":1.06},"A11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":74.24,"z":1.06},"B11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":65.24,"z":1.06},"C11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":56.24,"z":1.06},"D11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":47.24,"z":1.06},"E11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":38.24,"z":1.06},"F11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":29.24,"z":1.06},"G11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":20.24,"z":1.06},"H11":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":104.38,"y":11.24,"z":1.06},"A12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":74.24,"z":1.06},"B12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":65.24,"z":1.06},"C12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":56.24,"z":1.06},"D12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":47.24,"z":1.06},"E12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":38.24,"z":1.06},"F12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":29.24,"z":1.06},"G12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":20.24,"z":1.06},"H12":{"depth":20,"totalLiquidVolume":200,"shape":"circular","diameter":5.46,"x":113.38,"y":11.24,"z":1.06}},"groups":[{"metadata":{"wellBottomShape":"v"},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"individualpcrtubes_96_wellplate_200ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}},"custom_beta/opentrons_24_tall_tubes/1":{"ordering":[["A1","B1","C1","D1"],["A2","B2","C2","D2"],["A3","B3","C3","D3"],["A4","B4","C4","D4"],["A5","B5","C5","D5"],["A6","B6","C6","D6"]],"brand":{"brand":"Opentrons","brandId":[]},"metadata":{"displayName":"Opentrons 24 Tube Rack with 1.5mL Tall Tubes","displayCategory":"tubeRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.75,"yDimension":85.5,"zDimension":45},"wells":{"A1":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":18.21,"y":75.43,"z":1},"B1":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":18.21,"y":56.15,"z":1},"C1":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":18.21,"y":36.87,"z":1},"D1":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":18.21,"y":17.59,"z":1},"A2":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":38.1,"y":75.43,"z":1},"B2":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":38.1,"y":56.15,"z":1},"C2":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":38.1,"y":36.87,"z":1},"D2":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":38.1,"y":17.59,"z":1},"A3":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":57.99,"y":75.43,"z":1},"B3":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":57.99,"y":56.15,"z":1},"C3":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":57.99,"y":36.87,"z":1},"D3":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":57.99,"y":17.59,"z":1},"A4":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":77.88,"y":75.43,"z":1},"B4":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":77.88,"y":56.15,"z":1},"C4":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":77.88,"y":36.87,"z":1},"D4":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":77.88,"y":17.59,"z":1},"A5":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":97.77,"y":75.43,"z":1},"B5":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":97.77,"y":56.15,"z":1},"C5":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":97.77,"y":36.87,"z":1},"D5":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":97.77,"y":17.59,"z":1},"A6":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":117.66,"y":75.43,"z":1},"B6":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":117.66,"y":56.15,"z":1},"C6":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":117.66,"y":36.87,"z":1},"D6":{"depth":44,"totalLiquidVolume":1500,"shape":"circular","diameter":8,"x":117.66,"y":17.59,"z":1}},"groups":[{"metadata":{"wellBottomShape":"v","displayCategory":"tubeRack"},"wells":["A1","B1","C1","D1","A2","B2","C2","D2","A3","B3","C3","D3","A4","B4","C4","D4","A5","B5","C5","D5","A6","B6","C6","D6"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":false,"isMagneticModuleCompatible":false,"loadName":"opentrons_24_tall_tubes"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}}""")

DESIGNER_APPLICATION = """{"robot":{"model":"OT-2 Standard"},"designerApplication":{"name":"opentrons/protocol-designer","version":"8.6.0","data":{"pipetteTiprackAssignments":{"e62c3100-3f2d-4116-814f-769c04be56d4":["opentrons/opentrons_96_filtertiprack_200ul/1"],"73438296-41f8-44e2-b6ea-edce2448d720":["opentrons/opentrons_96_filtertiprack_20ul/1"]},"dismissedWarnings":{"form":["TIP_POSITIONED_LOW_IN_TUBE"],"timeline":["ASPIRATE_MORE_THAN_WELL_CONTENTS"]},"ingredients":{"0":{"displayName":"5x miRCURY","description":null,"displayColor":"#51ff4fff","liquidGroupId":"0","liquidClass":null},"1":{"displayName":"PCR Grade Water","description":null,"displayColor":"#0700ffff","liquidGroupId":"1","liquidClass":null},"2":{"displayName":"10x miRCURY","description":null,"displayColor":"#fb1f0eff","liquidGroupId":"2","liquidClass":null},"3":{"displayName":"Uni-Sp6","description":null,"displayColor":"#efff01ff","liquidGroupId":"3","liquidClass":null},"4":{"displayName":"miRNA 100uM","description":null,"displayColor":"#50d5ff","liquidGroupId":"4","liquidClass":null},"5":{"displayName":"2x miRCURY","description":null,"displayColor":"#fe1414ff","liquidGroupId":"5","liquidClass":null},"6":{"displayName":"U6 primer mix","description":null,"displayColor":"#edd511ff","liquidGroupId":"6","liquidClass":null},"7":{"displayName":"primer mix 2","description":null,"displayColor":"#389be6ff","liquidGroupId":"7","liquidClass":null},"8":{"displayName":"Sample","description":null,"displayColor":"#9dffd8ff","liquidGroupId":"8","liquidClass":null},"9":{"displayName":"gDNA Wipeout Buffer 7x","description":null,"displayColor":"#00d3ffff","liquidGroupId":"9","liquidClass":null},"10":{"displayName":"Quantiscript Reverse Transcriptase","description":null,"displayColor":"#ff5000ff","liquidGroupId":"10","liquidClass":null},"11":{"displayName":"RT Buffer","description":null,"displayColor":"#ac00ffff","liquidGroupId":"11","liquidClass":null},"12":{"displayName":"RT Primer Mix","description":null,"displayColor":"#ffc500ff","liquidGroupId":"12","liquidClass":null},"13":{"displayName":"2x QuantiNOVA SYBR Green PCR MM","description":null,"displayColor":"#12ed11ff","liquidGroupId":"13","liquidClass":null},"14":{"displayName":"Proprietary Primers","description":null,"displayColor":"#fff442ff","liquidGroupId":"14","liquidClass":null},"15":{"displayName":"IDT primers","description":null,"displayColor":"#9dffd8ff","liquidGroupId":"15","liquidClass":null},"16":{"displayName":"10uM Primer","displayColor":"#9dffd8ff","description":null,"liquidGroupId":"16"}},"ingredLocations":{"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2":{},"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1":{"A1":{"9":{"volume":100}},"A2":{"1":{"volume":1000}},"A3":{"10":{"volume":100}},"A4":{"11":{"volume":100}},"A6":{"13":{"volume":1000}},"B1":{"14":{"volume":1000}},"B2":{"14":{"volume":1000}}},"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1":{"D1":{"8":{"volume":10}},"D2":{"8":{"volume":10}},"D3":{"8":{"volume":10}},"D4":{"8":{"volume":10}},"D5":{"8":{"volume":10}},"D6":{"8":{"volume":10}}}},"savedStepForms":{"__INITIAL_DECK_SETUP_STEP__":{"labwareLocationUpdate":{"3498548b-01ab-431a-af64-66ccd8db4b5a:opentrons/opentrons_96_filtertiprack_200ul/1":"9","17bcbc7a-b4db-4709-83df-8da52004609d:opentrons/opentrons_96_filtertiprack_20ul/1":"8","f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2":"5","2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1":"1","e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1":"4","76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4":"2"},"moduleLocationUpdate":{},"pipetteLocationUpdate":{"e62c3100-3f2d-4116-814f-769c04be56d4":"left","73438296-41f8-44e2-b6ea-edce2448d720":"right"},"trashBinLocationUpdate":{"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin":"cutout12"},"wasteChuteLocationUpdate":{},"stagingAreaLocationUpdate":{},"gripperLocationUpdate":{},"stepType":"manualIntervention","id":"__INITIAL_DECK_SETUP_STEP__"},"17e8807b-4531-476e-9ee4-c104044fdd1d":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":10,"aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":2.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":3.78,"blowout_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":3.7,"dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":2.5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"16","stepType":"moveLiquid","stepName":"16uL GDNA Wipeout Master Mix","stepDetails":"","id":"17e8807b-4531-476e-9ee4-c104044fdd1d","dispense_touchTip_mmfromTop":null},"47dad0c5-50a3-4cdb-8f46-c94b3c526938":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":200,"aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":2.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":46.43,"blowout_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":200,"dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"35","dispense_mmFromBottom":2.5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"e62c3100-3f2d-4116-814f-769c04be56d4","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"88","stepType":"moveLiquid","stepName":"88uL RNAse Free Water","stepDetails":"","id":"47dad0c5-50a3-4cdb-8f46-c94b3c526938","dispense_touchTip_mmfromTop":null},"de0e41c4-77aa-4fcc-b809-84983bf822d1":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":3.7,"aspirate_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":3.78,"blowout_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":3.7,"dispense_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["G1","G2","G3","G4","G5","G6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"13","stepType":"moveLiquid","stepName":"13uL MM into each PCR tube","stepDetails":"","id":"de0e41c4-77aa-4fcc-b809-84983bf822d1","dispense_touchTip_mmfromTop":null},"208b7e03-8d01-4db6-85bc-48b594402434":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":true,"aspirate_delay_seconds":"3","aspirate_flowRate":20,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["D1","D2","D3","D4","D5","D6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":20,"dispense_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"2","dispense_mix_volume":"10","dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["G1","G2","G3","G4","G5","G6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL of Samp","stepDetails":"","id":"208b7e03-8d01-4db6-85bc-48b594402434","dispense_touchTip_mmfromTop":null},"e7665733-fca8-419f-8d9d-fe67ab129409":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Place PCR tubes with gDNA and sample mixtures onto the 42C heat block for 2 minutes and then place on ice. In the meantime, start the next portion of the protocol.","pauseTemperature":null,"pauseTime":null,"id":"e7665733-fca8-419f-8d9d-fe67ab129409","stepType":"pause","stepName":"pause","stepDetails":""},"90699357-a8fa-4938-a351-1138114bdb99":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":10,"aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":2.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":3.78,"blowout_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":3.7,"dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"8","stepType":"moveLiquid","stepName":"8uL RTase","stepDetails":"","id":"90699357-a8fa-4938-a351-1138114bdb99","dispense_touchTip_mmfromTop":null},"8c06ee38-ea75-4c9a-9864-1d1edc58738d":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":46.4,"aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":2.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":46.43,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":46.43,"dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A2"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"e62c3100-3f2d-4116-814f-769c04be56d4","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"40","stepType":"moveLiquid","stepName":"40uL Premix RT Buffer + RT Primer","stepDetails":"","id":"8c06ee38-ea75-4c9a-9864-1d1edc58738d","dispense_touchTip_mmfromTop":null},"187f7486-cd52-4ff8-9758-2755d7eede9f":{"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":46.4,"blowout_checkbox":false,"blowout_flowRate":46.43,"blowout_location":null,"blowout_z_offset":0,"changeTip":"always","dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":46.43,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","liquidClassesSupported":false,"liquidClass":"none","mix_mmFromBottom":1.5,"mix_touchTip_checkbox":false,"mix_touchTip_mmFromTop":null,"mix_wellOrder_first":"t2b","mix_wellOrder_second":"l2r","mix_position_reference":"well-bottom","mix_x_position":0,"mix_y_position":0,"nozzles":null,"pipette":"e62c3100-3f2d-4116-814f-769c04be56d4","pushOut_checkbox":false,"pushOut_volume":0,"times":"10","tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"35","wells":["A2"],"stepType":"mix","stepName":"Mixing RT MM","stepDetails":"","id":"187f7486-cd52-4ff8-9758-2755d7eede9f"},"f1b58b5e-22f6-497a-bfc2-46f66a2fbb53":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Remove PCR tubes from ice and place into individual PCR plate holder.","pauseTemperature":null,"pauseTime":null,"id":"f1b58b5e-22f6-497a-bfc2-46f66a2fbb53","stepType":"pause","stepName":"pause","stepDetails":""},"b365efdb-48e4-4fae-9929-e2fd7366ed71":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":10,"aspirate_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":10,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":20,"dispense_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","dispense_mix_checkbox":true,"dispense_mix_times":"6","dispense_mix_volume":"15","dispense_mmFromBottom":1.5,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["G1","G2","G3","G4","G5","G6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"6","stepType":"moveLiquid","stepName":"6uL RT MM into gDNA Wipeout","stepDetails":"","id":"b365efdb-48e4-4fae-9929-e2fd7366ed71","dispense_touchTip_mmfromTop":null},"63e6e327-fbe4-46ac-94ea-cc7bab914b76":{"moduleId":null,"pauseAction":"untilResume","pauseMessage":"Place PCR tubes with RTase and sample mixture on the 42C heatblock for 15 minutes and then place on the 95C heatblock for 3 minutes, and then place on ice. Remove gDNA wipeout (A1), RTase (A3), Premix RT (A4) and place into freezer. Once ready, load primers into machine.","pauseTemperature":null,"pauseTime":null,"id":"63e6e327-fbe4-46ac-94ea-cc7bab914b76","stepType":"pause","stepName":"pause","stepDetails":""},"e390fa98-68bf-4841-b3f0-2f9f734a24ee":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":77,"aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":2.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":46.43,"blowout_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":200,"dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"e62c3100-3f2d-4116-814f-769c04be56d4","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"240","stepType":"moveLiquid","stepName":"240uL 2x SYBR Green MM","stepDetails":"","id":"e390fa98-68bf-4841-b3f0-2f9f734a24ee","dispense_touchTip_mmfromTop":null},"34362f06-a088-4c54-9c2d-85c4cfa32c34":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":46.4,"aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":3,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["B1","B2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":46.43,"blowout_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":46.4,"dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":true,"dispense_mix_times":"2","dispense_mix_volume":"40","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"e62c3100-3f2d-4116-814f-769c04be56d4","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"48","stepType":"moveLiquid","stepName":"48uL Proprietary Forward Primer","stepDetails":"","id":"34362f06-a088-4c54-9c2d-85c4cfa32c34","dispense_touchTip_mmfromTop":null},"7208fae0-c8cc-4c73-b600-d7e0a8b790e9":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":"250","aspirate_labware":"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":2.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":46.43,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":"250","dispense_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","dispense_mix_checkbox":true,"dispense_mix_times":"10","dispense_mix_volume":"100","dispense_mmFromBottom":3,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A3","A4"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"e62c3100-3f2d-4116-814f-769c04be56d4","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_200ul/1","volume":"168","stepType":"moveLiquid","stepName":"168uL RNAse Free H2O","stepDetails":"","id":"7208fae0-c8cc-4c73-b600-d7e0a8b790e9","dispense_touchTip_mmfromTop":null},"ae62d12c-65bf-4385-8bf0-8f3d60cd3ded":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":12,"aspirate_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":22,"blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":12,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","B1","C1","D1","E1","F1","A2","B2","C2","D2","E2","F2","A3","B3","C3","D3","E3","F3"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"19","stepType":"moveLiquid","stepName":"19uL PCR 1 MM","stepDetails":"","id":"ae62d12c-65bf-4385-8bf0-8f3d60cd3ded","dispense_touchTip_mmfromTop":null},"f8b969a3-7852-44ac-9165-4299ec4fe009":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":12,"aspirate_labware":"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1.5,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["A4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":false,"blowout_flowRate":22,"blowout_location":"dest_well","changeTip":"once","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":12,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":false,"dispense_mix_times":null,"dispense_mix_volume":null,"dispense_mmFromBottom":1,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A4","B4","C4","D4","E4","F4","A5","B5","C5","D5","E5","F5","A6","B6","C6","D6","E6","F6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":false,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"19","stepType":"moveLiquid","stepName":"19uL PCR 2 MM","stepDetails":"","id":"f8b969a3-7852-44ac-9165-4299ec4fe009","dispense_touchTip_mmfromTop":null},"4bb30493-2416-4f29-a30f-94c92ce99548":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":6,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G1"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":10,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"8","dispense_mmFromBottom":0.2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["A1","A2","A3","A4","A5","A6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL cDNA Samps","stepDetails":"","id":"4bb30493-2416-4f29-a30f-94c92ce99548","dispense_touchTip_mmfromTop":null},"d0e93338-73d1-4c49-90aa-fc69d85e9b16":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":6,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G2"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":10,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"8","dispense_mmFromBottom":0.2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["B1","B2","B3","B4","B5","B6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL cDNA Samps","stepDetails":"","id":"d0e93338-73d1-4c49-90aa-fc69d85e9b16","dispense_touchTip_mmfromTop":null},"5828c459-eded-4b9c-bd09-6589e4dc9757":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":6,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G3"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":10,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"8","dispense_mmFromBottom":0.2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["C1","C2","C3","C4","C5","C6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL cDNA Samps","stepDetails":"","id":"5828c459-eded-4b9c-bd09-6589e4dc9757","dispense_touchTip_mmfromTop":null},"3bb0c22c-de48-4204-99e0-07e07291fa44":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":6,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G4"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":10,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"8","dispense_mmFromBottom":0.2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["D1","D2","D3","D4","D5","D6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL cDNA Samps","stepDetails":"","id":"3bb0c22c-de48-4204-99e0-07e07291fa44","dispense_touchTip_mmfromTop":null},"f4da1e36-766f-41c7-91d5-436d5cb91aca":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":6,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G5"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":10,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"8","dispense_mmFromBottom":0.2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["E1","E2","E3","E4","E5","E6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL cDNA Samps","stepDetails":"","id":"f4da1e36-766f-41c7-91d5-436d5cb91aca","dispense_touchTip_mmfromTop":null},"e3c14c29-5c0d-44c2-840d-658fd9392fa5":{"aspirate_airGap_checkbox":false,"aspirate_airGap_volume":null,"aspirate_delay_checkbox":false,"aspirate_delay_seconds":"1","aspirate_flowRate":6,"aspirate_labware":"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1","aspirate_mix_checkbox":false,"aspirate_mix_times":null,"aspirate_mix_volume":null,"aspirate_mmFromBottom":1,"aspirate_position_reference":"well-bottom","aspirate_retract_delay_seconds":0,"aspirate_retract_mmFromBottom":2,"aspirate_retract_speed":125,"aspirate_retract_x_position":null,"aspirate_retract_y_position":null,"aspirate_retract_position_reference":"well-top","aspirate_submerge_delay_seconds":0,"aspirate_submerge_speed":125,"aspirate_submerge_mmFromBottom":2,"aspirate_submerge_x_position":null,"aspirate_submerge_y_position":null,"aspirate_submerge_position_reference":"well-top","aspirate_touchTip_checkbox":false,"aspirate_touchTip_mmFromTop":null,"aspirate_touchTip_speed":400,"aspirate_touchTip_mmFromEdge":0,"aspirate_wellOrder_first":"t2b","aspirate_wellOrder_second":"l2r","aspirate_wells_grouped":false,"aspirate_wells":["G6"],"aspirate_x_position":0,"aspirate_y_position":0,"blowout_checkbox":true,"blowout_flowRate":3.78,"blowout_location":"dest_well","changeTip":"always","conditioning_checkbox":false,"conditioning_volume":null,"dispense_airGap_checkbox":false,"dispense_airGap_volume":null,"dispense_delay_checkbox":false,"dispense_delay_seconds":"1","dispense_flowRate":10,"dispense_labware":"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4","dispense_mix_checkbox":true,"dispense_mix_times":"3","dispense_mix_volume":"8","dispense_mmFromBottom":0.2,"dispense_position_reference":"well-bottom","dispense_retract_delay_seconds":0,"dispense_retract_mmFromBottom":2,"dispense_retract_speed":125,"dispense_retract_x_position":null,"dispense_retract_y_position":null,"dispense_retract_position_reference":"well-top","dispense_submerge_delay_seconds":0,"dispense_submerge_speed":125,"dispense_submerge_mmFromBottom":2,"dispense_submerge_x_position":null,"dispense_submerge_y_position":null,"dispense_submerge_position_reference":"well-top","dispense_touchTip_checkbox":false,"dispense_touchTip_mmFromTop":null,"dispense_touchTip_speed":400,"dispense_touchTip_mmFromEdge":0,"dispense_wellOrder_first":"t2b","dispense_wellOrder_second":"l2r","dispense_wells":["F1","F2","F3","F4","F5","F6"],"dispense_x_position":0,"dispense_y_position":0,"disposalVolume_checkbox":true,"disposalVolume_volume":null,"dropTip_location":"6fb4f96c-6dcc-40a7-8ca2-e1c6c1e138aa:trashBin","liquidClassesSupported":false,"liquidClass":"none","nozzles":null,"path":"single","pipette":"73438296-41f8-44e2-b6ea-edce2448d720","preWetTip":true,"pushOut_checkbox":false,"pushOut_volume":0,"tipRack":"opentrons/opentrons_96_filtertiprack_20ul/1","volume":"1","stepType":"moveLiquid","stepName":"1uL cDNA Samps","stepDetails":"","id":"e3c14c29-5c0d-44c2-840d-658fd9392fa5","dispense_touchTip_mmfromTop":null}},"orderedStepIds":["17e8807b-4531-476e-9ee4-c104044fdd1d","47dad0c5-50a3-4cdb-8f46-c94b3c526938","de0e41c4-77aa-4fcc-b809-84983bf822d1","208b7e03-8d01-4db6-85bc-48b594402434","e7665733-fca8-419f-8d9d-fe67ab129409","90699357-a8fa-4938-a351-1138114bdb99","8c06ee38-ea75-4c9a-9864-1d1edc58738d","187f7486-cd52-4ff8-9758-2755d7eede9f","f1b58b5e-22f6-497a-bfc2-46f66a2fbb53","b365efdb-48e4-4fae-9929-e2fd7366ed71","63e6e327-fbe4-46ac-94ea-cc7bab914b76","e390fa98-68bf-4841-b3f0-2f9f734a24ee","34362f06-a088-4c54-9c2d-85c4cfa32c34","7208fae0-c8cc-4c73-b600-d7e0a8b790e9","ae62d12c-65bf-4385-8bf0-8f3d60cd3ded","f8b969a3-7852-44ac-9165-4299ec4fe009","4bb30493-2416-4f29-a30f-94c92ce99548","d0e93338-73d1-4c49-90aa-fc69d85e9b16","5828c459-eded-4b9c-bd09-6589e4dc9757","3bb0c22c-de48-4204-99e0-07e07291fa44","f4da1e36-766f-41c7-91d5-436d5cb91aca","e3c14c29-5c0d-44c2-840d-658fd9392fa5"],"pipettes":{"e62c3100-3f2d-4116-814f-769c04be56d4":{"pipetteName":"p300_single_gen2"},"73438296-41f8-44e2-b6ea-edce2448d720":{"pipetteName":"p20_single_gen2"}},"modules":{},"labware":{"3498548b-01ab-431a-af64-66ccd8db4b5a:opentrons/opentrons_96_filtertiprack_200ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 200 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_200ul/1"},"17bcbc7a-b4db-4709-83df-8da52004609d:opentrons/opentrons_96_filtertiprack_20ul/1":{"displayName":"Opentrons OT-2 96 Filter Tip Rack 20 µL","labwareDefURI":"opentrons/opentrons_96_filtertiprack_20ul/1"},"f9b2f84e-593c-4d9d-8a57-8c1b15ed413b:opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2":{"displayName":"Opentrons 24 Tube Rack with Eppendorf 1.5 mL Safe-Lock Snapcap","labwareDefURI":"opentrons/opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap/2"},"2ab67ace-8c78-4004-a266-fd629bd874a4:custom_beta/individualpcrtubes_96_wellplate_200ul/1":{"displayName":"Individual PCR Tubes 96 Well Plate 200 µL","labwareDefURI":"custom_beta/individualpcrtubes_96_wellplate_200ul/1"},"e518b83a-3c6d-49e3-b323-c273e01c27b2:custom_beta/opentrons_24_tall_tubes/1":{"displayName":"Opentrons 24 Tube Rack with 1.5mL Tall Tubes","labwareDefURI":"custom_beta/opentrons_24_tall_tubes/1"},"76273b05-de63-4478-9544-e68023f1c68a:opentrons/biorad_96_wellplate_200ul_pcr/4":{"displayName":"Bio-Rad 96 Well Plate 200 µL PCR","labwareDefURI":"opentrons/biorad_96_wellplate_200ul_pcr/4"}}}},"metadata":{"protocolName":"103025 1 Joy Combined RTPCR TVasse 6samps (2 Proprietary Primers)","author":"Tyler Vasse","description":"","created":1744049701428,"lastModified":1761847374561,"category":null,"subcategory":null,"tags":[],"source":"Protocol Designer"}}"""
