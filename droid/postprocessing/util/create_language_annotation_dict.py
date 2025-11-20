import os
import json
import argparse

def build_annotations(data_dir, output_path):
    annotations = {}
    for dir in os.listdir(data_dir):
        for fname in os.listdir(dir):
            if fname.endswith(".json"):
                print(fname)
                meta_path = os.path.join(data_dir, dir, fname)
                with open(meta_path, "r") as f:
                    meta = json.load(f)
                stem = os.path.splitext(fname)[0]
                episode_id = stem.split("_")[-1]

                current_task = meta.get("current_task", None)
                if not isinstance(current_task, str) or not current_task.strip():
                    print(f"[WARNING] no valid current task in {fname}. Skipping.")
                    continue
                
                annotations[episode_id] = {
                    "language_instruction1": current_task.strip()
                }

    with open(output_path, "w") as f:
        json.dump(annotations, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(annotations)} annotations to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create DROID-Style aggregated-annotations JSON from metadata_* files"
    )
    parser.add_argument(
        "--metadata_dir",
        type=str,
        required=True
    )
    parser.add_argument(
        "--output_file",
        type=str,
        default="aggregated-annotations-custom.json",
    )

    args = parser.parse_args()
    build_annotations(args.metadata_dir, args.output_file)