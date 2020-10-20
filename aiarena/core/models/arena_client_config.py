from django.db import models

from . import ArenaClient


class ArenaClientConfig(models.Model):
    """The ArenaClient this config pertains to"""
    arenaclient = models.ForeignKey(ArenaClient, on_delete=models.CASCADE)
    """How many matches to run before restarting"""
    ROUNDS_PER_RUN = models.IntegerField(default=5)
    """Write .shutdown file after matches have run"""
    SHUTDOWN_AFTER_RUN = models.BooleanField(default=True)
    """More debug logging"""
    DEBUG_MODE = models.BooleanField(default=False)
    """Which Python to use to start bots"""
    PYTHON = models.CharField(default="python3", max_length=10)
    """Clean up directories after each match"""
    CLEANUP_BETWEEN_ROUNDS = models.BooleanField(default=True)
    """Run in secure mode (separated users and directories"""
    SECURE_MODE = models.BooleanField(default=False)
    """User name for player 1 if running in secure mode"""
    RUN_PLAYER1_AS_USER = models.CharField(max_length=50)
    """User name for player 2 if running in secure mode"""
    RUN_PLAYER2_AS_USER = models.CharField(max_length=50)
    """Logging level for logs. (Debug = 10, Info =20, Warning = 30)"""
    LOGGING_LEVEL = models.IntegerField(default=10)
    """Max in game time in frames"""
    MAX_GAME_TIME = models.IntegerField(default=68486)
    """Max real time for a match in seconds"""
    MAX_REAL_TIME = models.IntegerField(default=7200)
    """Max frame time for a bot in ms"""
    MAX_FRAME_TIME = models.IntegerField(default=1000)
    """How many times a bot can go over max frame time before being timed out"""
    STRIKES = models.IntegerField(default=10)
    """Run SC2 in realtime mode"""
    REALTIME = models.BooleanField(default=False)
    """Disable debug interface"""
    DISABLE_DEBUG = models.BooleanField(default=True)
    """Validate bot race with race on website"""
    VALIDATE_RACE = models.BooleanField(default=False)
