#!/bin/zsh

########################################################
# Selected Factors with different window sizes
########################################################

# Parameters
outputLocation="/work/eg474423/ig440396_dendriticcells/local/mast/MotifStatistics/"
organism="-organism=mm9"
motif_match_fpr="-motif_match_fpr=0.001"
rand_proportion_size="-rand_proportion_size=1.0"
print_association="-print_association=Y"
print_mpbs="-print_mpbs=N"
print_results_text="-print_results_text=Y"
print_results_html="-print_results_html=Y"
print_enriched_genes="-print_enriched_genes=N"
print_rand_coordinates="-print_rand_coordinates=Y"
print_graph_mmscore="-print_graph_mmscore=N"

# Variations
cl="/work/eg474423/ig440396_dendriticcells/local/mast/Input/"
gl="/work/eg474423/ig440396_dendriticcells/local/mast/GeneList/"
wSizeList=( "200" "500" "1000" )
geneList=( "naive_lps" "tolerance" "tolerance_control" "tolerance_lps" )

# Execution
for wSize in $wSizeList
do

    coord_file="-coord_file="$cl"mm9_promoters_"$wSize".bed"

    for geneFile in $geneList
    do

        gene_list="-gene_list="$gl$geneFile".txt"
        outLoc=$outputLocation$wSize"/"$geneFile"/"
        output_location="-output_location="$outLoc
        mkdir -p $outLoc
        
        bsub -J $geneFile"_"$wSize"_MS" -o $geneFile"_"$wSize"_MS_out.txt" -e $geneFile"_"$wSize"_MS_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./motifStatistics_pipeline.zsh $coord_file $gene_list $output_location $organism $motif_match_fpr $rand_proportion_size $print_association $print_mpbs $print_results_text $print_results_html $print_enriched_genes $print_rand_coordinates $print_graph_mmscore

    done
done


