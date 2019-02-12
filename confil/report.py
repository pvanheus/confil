import os

import click


def parse_report(report_file, cutoff):
    file_name = os.path.splitext(os.path.basename(report_file))[0]
    hit = None
    if os.stat(report_file).st_size > 0 and report_file.endswith(".report"):
        click.secho("Processing {} with cutoff of {}...\n".format(
            report_file, cutoff), fg='green')
        with open(report_file, 'r') as report:
            for line in report:
                line = [str(e).strip() for e in line.split('\t')]
                if len(line) > 1:
                    click.secho('{}'.format(line), fg='green')
                    # Percentage of fragments covered by the clade rooted at this taxon
                    percentage = int(float(line[0]))
                    # Number of fragments covered by the clade rooted at this taxon
                    # num_covered = int(float(line[1]))
                    # Number of fragments assigned directly to this taxon
                    # num_assigned = int(float(line[2]))
                    # NCBI taxonomic ID number
                    # ncbi_tax = int(float(line[3]))
                    # Indented scientific name (Mycobacterium\n)
                    name = str(line[5]).strip()
                    if percentage < cutoff and 'Mycobacterium' in name:
                        click.secho('\n{}%: {} is contaminated!\n'.format(
                            percentage, file_name), fg='red')
                        raise SystemExit('{}%: {} is contaminated!\n'.format(
                            percentage, file_name))
                    if percentage >= cutoff and 'Mycobacterium' in name:
                        click.secho('\n{}%: {} is not contaminated!\n'.format(
                            percentage, file_name), fg='green')
                        hit = line
                        break
    click.secho('Hit: {}'.format(hit), fg='green')
    return hit
