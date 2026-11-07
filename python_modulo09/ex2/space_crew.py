
from enum import Enum
from datetime import datetime
from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with M")

        has_leader: bool = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )

        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced: int = sum(
                1
                for member in self.crew
                if member.years_experience >= 5
            )

            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions require at least 50% "
                    "experienced crew (5+ years)"
                )

        all_active: bool = all(
            member.is_active for member in self.crew
        )

        if not all_active:
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 41)

    print("\nValid mission created:")

    mission = SpaceMission(
        mission_id="M2024",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2027, 5, 15, 10, 30),
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=45,
                specialization="Mission Command",
                years_experience=15,
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=30,
                specialization="Engineering",
                years_experience=2,
            ),
        ],
    )

    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")

    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )

    print("=" * 41)
    print("\nExpected validation error:")

    try:
        SpaceMission(
            mission_id="M2025",
            mission_name="Moon Exploration",
            destination="Moon",
            launch_date=datetime(2027, 8, 20),
            duration_days=100,
            budget_millions=500.0,
            crew=[
                CrewMember(
                    member_id="C004",
                    name="Peter Parker",
                    rank=Rank.OFFICER,
                    age=28,
                    specialization="Research",
                    years_experience=5,
                ),
                CrewMember(
                    member_id="C005",
                    name="Bruce Wayne",
                    rank=Rank.LIEUTENANT,
                    age=40,
                    specialization="Engineering",
                    years_experience=10,
                ),
            ],
        )

    except ValidationError as error:
        print(error)


if __name__ == "__main__":
    main()
