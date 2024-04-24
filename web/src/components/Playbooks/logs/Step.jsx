import styles from "../playbooks.module.css";
import { Launch } from "@mui/icons-material";
import Notes from "../steps/Notes.jsx";
import Query from "./Query.jsx";

function Step({ step, index }) {
  return (
    <div className={styles["step-card"]}>
      <div className={styles["step-card-content"]} style={{ padding: "0px" }}>
        <div className={styles["step-name"]}>
          <div className={styles.head}>
            <div className={styles.extLinks}>
              {step.externalLinks?.map((link, i) => (
                <a
                  key={i}
                  href={link.url}
                  target="_blank"
                  rel="noreferrer"
                  className={styles.extLink}>
                  {link?.name || link.url} <Launch />
                </a>
              ))}
            </div>
          </div>
        </div>
        <div className={styles["step-section"]}>
          {step.notes && (
            <>
              <div className={styles["addConditionStyle"]}>
                <b>Notes</b>
              </div>
              <Notes step={step} index={index} />
            </>
          )}
          <div className={styles["step-info"]}>
            {step.source && (
              <div>
                <div className={styles["addConditionStyle"]}>
                  <b>Data</b>
                </div>

                <Query step={step} index={index} />
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Step;