<properties 
	pageTitle="Testing a runbook in Azure Automation | Azure"
	description="Before you publish a runbook in Azure Automation, you can test it to ensure that works as expected.  This article describes how to test a runbook and view its output."
	services="automation"
	documentationCenter=""
	authors="mgoedtel"
	manager="jwhit"
	editor="tysonn" />
<tags
	ms.service="automation"
	ms.date="05/24/2016"
	wacn.date=""/>

# Testing a runbook in Azure Automation
When you test a runbook, the [Draft version](/documentation/articles/automation-creating-importing-runbook/#publishing-a-runbook) is executed and any actions that it performs are completed. No job history is created, but the [Output](/documentation/articles/automation-runbook-output-and-messages/#output-stream) and [Warning and Error](/documentation/articles/automation-runbook-output-and-messages/#message-streams) streams are displayed in the Test output Pane. Messages to the [Verbose Stream](/documentation/articles/automation-runbook-output-and-messages/#message-streams) are displayed in the Output Pane only if the [$VerbosePreference variable](/documentation/articles/automation-runbook-output-and-messages/#preference-variables) is set to Continue.

Even though the draft version is being run, the runbook still executes the workflow normally and performs any actions against resources in the environment. For this reason, you should only test runbooks at non-production resources.

## To test a runbook in the Azure Classic Management Portal

1. [Open the Draft version of the runbook](/documentation/articles/automation-edit-textual-runbook/#to-edit-a-runbook-with-the-azure-portal).
2. Click the **Test** button to start the test.  If the runbook has parameters, you will receive a dialog box to provide values to be used for the test.
6. You can stop or suspend the runbook while it is being tested with the buttons underneath the Output Pane. When you suspend the runbook, it completes the current activity before being suspended. Once the runbook is suspended, you can stop it or restart it.
7. Inspect the output from the runbook in the output pane.

## Next Steps

- To learn how to create or import a runbook, see [Creating or importing a runbook in Azure Automation](/documentation/articles/automation-creating-importing-runbook/)
- To get started with PowerShell workflow runbooks, see [My first PowerShell workflow runbook](/documentation/articles/automation-first-runbook-textual/)
- To learn more about configuring runboks to return status messages and errors, including recommended practices, see [Runbook output and messages in Azure Automation](/documentation/articles/automation-runbook-output-and-messages/)