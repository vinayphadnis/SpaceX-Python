# Declare URL Variables over here to be used to make requests


class Domain:
# general url to make request
    main = "https://api.spacexdata.com/v2/"

    # declaration of the endpoints
    # launches
    main_launches = "launches"
    latest_launches = main_launches + "/latest"
    next_launches =  main_launches + "/next"
    upcoming_launches = main_launches + "/upcoming"

    # rockets
    main_rockets = "rockets"
    falcon_1 = main_rockets + "/falcon1"
    falcon_9 = main_rockets + "/falcon9"
    falcon_heavy = main_rockets + "/falconheavy"
    big_falcon_rocket = main_rockets + "/bfr"

    # capsules
    main_capsules = "capsules"
    
