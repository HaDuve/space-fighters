import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Space fighters",
    options={"build_exe": {"packages": ["pygame","sys"],
        "include_files":["main4players.py", "resources/background.png", 'resources/ship1.png',
                          'resources/ship2.png','resources/ship3.png',
                          'resources/ship4.png', 'resources/rocket1.png',
                          'resources/rocket2.png', 'resources/rocket3.png',
                          'resources/rocket4.png', 'resources/endgamescreen1600.png',
                          'resources/lukas_powerup.png', 'resources/explosion.png',
                          'resources/ship1_lightspeed.png', 'resources/spacemine.png',
                          'resources/ship1_phantom.png', 'resources/ship2_lightspeed.png',
                          'resources/spacemine.png', 'resources/ship2_phantom.png',
                          'resources/ship3_lightspeed.png', 'resources/spacemine.png',
                          'resources/ship3_phantom.png', 'resources/ship4_lightspeed.png',
                          'resources/spacemine.png', 'resources/ship4_phantom.png'
                          ]}},
    executables=executables
)
