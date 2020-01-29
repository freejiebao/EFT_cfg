from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'VBS_SSWW_BSM_Premix_2'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SMP-Premix-BSM_2_cfg.py'
config.JobType.numCores = 4
config.JobType.maxMemoryMB = 6000

config.Data.inputDataset = '/Bulk/jixiao-VBS_SSWW_BSM_RAWSIMoutput-463d45b48c2a8dcb7ad3f636e9bc356e/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/eft2018' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'VBS_SSWW_BSM_Premix_2'

config.Site.storageSite = 'T2_CN_Beijing'
