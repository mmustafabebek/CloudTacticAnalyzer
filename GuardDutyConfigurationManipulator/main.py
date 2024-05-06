import boto3

def misconfigure_detector(detector_id, option):
    if option == 'a':
        # Disabling the detector
        cli_command = f"aws guardduty update-detector --detector-id {detector_id} --no-enable"
    elif option == 'b':
        # Removing S3 as a log source
        cli_command = f"aws guardduty update-detector --detector-id {detector_id} --data-sources S3Logs={{Enable=false}}"
    elif option == 'c':
        # Increase finding update time to 6 hours
        cli_command = f"aws guardduty update-detector --detector-id {detector_id} --finding-publishing-frequency SIX_HOURS"
    else:
        cli_command = "Invalid option"
    return cli_command

def modify_trusted_ip_lists(detector_id, ip_set_id, location):
    # Modify trusted IP lists
    cli_command = f"aws guardduty update-ip-set --detector-id {detector_id} --ip-set-id {ip_set_id} --location {location} --activate"
    return cli_command

def modify_cloudwatch_events_rule(option):
    if option == 'a':
        # Disable GuardDuty CloudWatch Event
        cli_command = "aws events put-rule --name guardduty-event --event-pattern '{\"source\":[\"aws.guardduty\"]}' --state DISABLED"
    elif option == 'b':
        # Modify Event Pattern
        cli_command = "aws events put-rule --name guardduty-event --event-pattern '{\"source\": [\"aws.somethingthatdoesntexist\"]}'"
    elif option == 'c':
        # Remove Event Targets
        cli_command = "aws events remove-targets --name guardduty-event --ids \"GuardDutyTarget\""
    else:
        cli_command = "Invalid option"
    return cli_command

def create_suppression_rule(detector_id):
    # Create suppression rule
    cli_command = f"aws guardduty create-filter --action ARCHIVE --detector-id {detector_id} --name yourfiltername --finding-criteria file://criteria.json"
    return cli_command

def delete_publishing_destination(detector_id, destination_id):
    # Delete publishing destination
    cli_command = f"aws guardduty delete-publishing-destination --detector-id {detector_id} --destination-id {destination_id}"
    return cli_command

def main():
    detector_id = input("Enter the detector ID: ")

    print("\nOptions:")
    print("1- Misconfiguring the Detector")
    print("2- Modifying Trusted IP Lists")
    print("3- Modify CloudWatch Events Rule")
    print("4- Suppression Rules")
    print("5- Delete Publishing Destination")

    option = input("\nEnter your choice: ")

    if option == '1':
        print("\na- Disabling the detector")
        print("b- Removing S3 as a log source")
        print("c- Increase finding update time to 6 hours\n")
        sub_option = input("Enter your choice: \n")
        cli_command = misconfigure_detector(detector_id, sub_option)
    elif option == '2':
        ip_set_id = input("\nEnter the IP set ID: ")
        location = input("Enter the location of the custom IP list: ")
        cli_command = modify_trusted_ip_lists(detector_id, ip_set_id, location)
    elif option == '3':
        print("\na- Disable GuardDuty CloudWatch Event")
        print("b- Modify Event Pattern")
        print("c- Remove Event Targets")
        sub_option = input("\nEnter your choice: ")
        cli_command = modify_cloudwatch_events_rule(sub_option)
    elif option == '4':
        cli_command = create_suppression_rule(detector_id)
    elif option == '5':
        destination_id = input("\nEnter the destination ID: ")
        cli_command = delete_publishing_destination(detector_id, destination_id)
    else:
        cli_command = "Invalid option"

    print("\nCli Command:")
    print(cli_command)

if __name__ == "__main__":
    main()
